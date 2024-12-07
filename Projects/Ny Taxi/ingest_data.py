import logging
import os
from time import time

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import bigquery

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)


def download_data(url, file_dir):
    """
    Download data dari URL dan simpan ke file_dir.

    Parameters:
    -----------
    url : str
        URL sumber data
    file_dir : str
        Direktori penyimpanan file
    max_rows : int, optional
        Jumlah maksimal baris yang akan dibaca

    Returns:
    --------
    pd.DataFrame
        DataFrame yang telah dibaca
    """
    # Pastikan folder 'data' ada
    os.makedirs("./data", exist_ok=True)

    try:
        # Periksa apakah file sudah ada
        if os.path.exists(file_dir):
            # Baca file Parquet dengan pembatasan rows
            df = pq.read_table(file_dir).to_pandas()

        else:
            # Unduh file jika belum ada
            logging.info(f"Mengunduh file dari {url}")
            os.system(f"wget {url} -O {file_dir}")
            logging.info("Unduhan selesai.")

            # Baca file dengan pembatasan rows
            table = pq.read_table(file_dir).to_pandas()

        logging.info(f"Total baris data: {len(df)}")
        return df

    except Exception as e:
        logging.error(f"Error dalam download_data: {e}")
        raise


def transform_nytaxi(df: pd.DataFrame) -> dict:
    """
    Transform yellow_tripdata_2024_05 tabel menjadi DataFrame bersih,
    dan buat dua tabel dimensi tambahan: rate_code_dim dan payment_type_dim

    Parameters
    ----------
    df : pd.DataFrame
        Tabel yellow_tripdata_2024_05

    Returns
    -------
    dict
        Dictionary berisi tiga dataframe
    """
    try:
        # Pembersihan data dengan validasi
        df = df[
            (df["passenger_count"] > 0)
            & (df["trip_distance"] > 0)
            & (df["total_amount"] > 0)
        ]

        # Hapus duplikat jika ada
        df.drop_duplicates(inplace=True)

        # Reset index
        df = df.reset_index(drop=True)
        df["trip_id"] = df.index

        # Pilih kolom yang relevan
        df = df[
            [
                "trip_id",
                "VendorID",
                "tpep_pickup_datetime",
                "tpep_dropoff_datetime",
                "passenger_count",
                "trip_distance",
                "RatecodeID",
                "store_and_fwd_flag",
                "PULocationID",
                "DOLocationID",
                "payment_type",
                "fare_amount",
                "extra",
                "mta_tax",
                "tip_amount",
                "tolls_amount",
                "improvement_surcharge",
                "total_amount",
                "congestion_surcharge",
                "Airport_fee",
            ]
        ]

        # Dimensional Tables
        rate_code_dim = df[["RatecodeID"]].drop_duplicates().reset_index(drop=True)

        mapping = {
            1: "Standard Rate",
            2: "JFK",
            3: "Newark",
            4: "Nassau or Westchester",
            5: "Negotiated fare",
            6: "Group ride",
        }

        rate_code_dim["rate_code_type"] = rate_code_dim["RatecodeID"].map(mapping)

        rate_code_dim = rate_code_dim[["RatecodeID", "rate_code_type"]]

        payment_type_dim = df[["payment_type"]].drop_duplicates().reset_index(drop=True)

        mapping = {
            1: "Credit card",
            2: "Cash",
            3: "No charge",
            4: "Dispute",
            5: "Unknown",
            6: "Voided trip",
        }

        payment_type_dim["payment_type_name"] = payment_type_dim["payment_type"].map(
            mapping
        )
        payment_type_dim = payment_type_dim[["payment_type", "payment_type_name"]]

        vendor_dim = df[["VendorID"]].drop_duplicates().reset_index(drop=True)

        mapping = {1: "Creative Mobile Technologies, LLC", 2: "VeriFone Inc."}

        vendor_dim["vendor_provider"] = vendor_dim["VendorID"].map(mapping)
        vendor_dim = vendor_dim[["VendorID", "vendor_provider"]]

        return {
            "yellow_tripdata_2024_05": df,
            "vendor_dim": vendor_dim,
            "rate_code_dim": rate_code_dim,
            "payment_type_dim": payment_type_dim,
        }

    except Exception as e:
        logging.error(f"Error dalam transform_nytaxi: {e}")
        raise


def upload_df_to_bigquery(data, write_disposition="WRITE_TRUNCATE"):
    """
    Upload dataframes ke BigQuery dengan konfigurasi tambahan.

    Args:
        data (dict): dictionary dengan nama tabel sebagai key dan dataframe sebagai value
        write_disposition (str, optional): metode penulisan di BigQuery
    """
    client = bigquery.Client()

    try:
        for table_name, df in data.items():
            t_start = time()
            logging.info(f"Inserting: {table_name} .....")

            table_id = f"firdauszakyy-de.yellow_trips_data.{table_name}"

            # Konfigurasi job
            job_config = bigquery.LoadJobConfig(
                write_disposition=write_disposition,
            )

            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)

            # Tunggu job selesai
            job.result()

            t_stop = time()
            logging.info(
                f"Upload {table_name} selesai dalam {t_stop - t_start:.2f} detik"
            )

    except Exception as e:
        logging.error(f"Error selama upload: {e}")
    else:
        logging.info("SEMUA PROSES SELESAI")


if __name__ == "__main__":
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-05.parquet"
    file_dir = "./data/" + url.split("/")[-1].replace("-", "_")

    # Batasi hanya 100.000 baris
    df = download_data(url, file_dir)

    # Transform data
    data = transform_nytaxi(df)

    # Upload ke BigQuery
    upload_df_to_bigquery(data)
