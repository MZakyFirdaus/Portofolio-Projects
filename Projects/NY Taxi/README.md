# NYC Taxi Projects

### Project Overview   
This project is a hands-on from [Data Engineering Zoomcamp 2024](https://github.com/DataTalksClub/data-engineering-zoomcamp) that I attended to learn about data engineering.    
In this project, we will do Extract, Transform, Load (ETL); understand the travel patterns of yellow taxis in New York City, such as pick hours, most frequent pick-up locations, when is the best day to do advertising.

### Architecture
- Data Source: NYC Taxi & Limousine Commission
- Data Orchestrator: Mage.AI
- Storage: Google Cloud BigQuery, PostgreSQL
- Infrastructure & Scalability: GCP

### Data Sources
The data used in this project comes from the NYC Taxi & Limousine Commission website specifically in May 2024.    
You can find it at:
- Yellow Taxi Data: <https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page>
- Zones data: <https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv>
- Details about the data: <https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf>

Brief explanation of the data:
- Yellow Taxi data:   
The New York City Yellow Taxi dataset is a collection of yellow taxi trip records since 2009 reported to the NYC Taxi and Limousine Commission (TLC).   
The data includes both traditional (street hail) and e-hail trips via apps like Curb or Arro. Each record details the pick-up/drop-off time and location, distance traveled, cost, fare type, payment method, and number of passengers. Yellow Taxi is the only taxi authorized to serve street hail pickups in all five boroughs of New York City.
- Zones data:   
Zones data in the Yellow Taxi New York City dataset is a collection of information on pick-up and drop-off locations identified through zone codes assigned by the NYC Taxi and Limousine Commission (TLC). These zones cover geographic areas in the five boroughs of New York City such as Manhattan, Brooklyn, Queens, Bronx, and Staten Island.

### Technology Used
Programming Language: 
- `Python` 
- `SQL`

Library: 
- `Pyarrow` 
- `Pandas` 

Google Cloud Platform:  
1. `Cloud Storage` as **Data Lake**
2. `Google Big Query` as **Data Warehouse**
3. `Looker Studio` to **Visualization**

Data Pipeline -- <https://docs.mage.ai/getting-started/setup>

### Data Pipeline
Proses ETL dalam projek ini menggunakan Mage AI sebagai data orkestrator. Mage AI adalah alternatif dari Apache Airflow untuk Data Pipeline.  

Untuk menggunakan Mage ai, anda bisa masuk ke [Getting Started With Mage.AI](https://docs.mage.ai/getting-started/setup#docker-compose). Pada Project ini akan digunakan `Docker` untuk setup Mage.Ai. 

Pertama, buat `Dockerfile` dan `docker-compose.yaml` dan mengatur `.env` file untuk konfigurasi.

```docker
FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

# Note: this overwrites the requirements.txt file in your new project on first run. 
# You can delete this line for the second run :) 
COPY requirements.txt ${USER_CODE_PATH}/requirements.txt 

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
```

Untuk konfigurasi `.env` file, atur nama project dan tempat anda menyimpan file google credentials. Semua yang ada di dalam .env file disini tentunya akan digunakan oleh `dokcer-compose.yaml`

```yaml
version: '3'
services:
  magic:
    image: mageai/mageai:latest
    command: mage start ${PROJECT_NAME}
    env_file:
      - .env
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      USER_CODE_PATH: /home/src/${PROJECT_NAME}
      ENV: ${ENV}
    ports:
      - 6789:6789
    volumes:
      - .:/home/src/
      - "${GOOGLE_CREDS_PATH}:/home/src/credentials.json"
    restart: on-failure:5
```
Untuk pertama kali, ini akan memakan beberapa menit untuk install image dan running container. Namun, setelah itu anda akan langsung bisa menggunakan mage.ai.   
Setelah containner running, navigasi ke <http://localhost:6789/> untuk membuka Mage AI.

#### Extract 
Untuk proses Extract dalam ETL pada projek ini, anda bisa melihat codenya di [extract_data.py](https://github.com/MZakyFirdaus/Portofolio-Projects/blob/main/Projects/NY%20Taxi/mage-files/loader/extract_data.py). Dalam proses ini, kita download file yang terdapat dalam URL karena hingga saat ini dibuat, `pyarrow` library belum bisa membaca parquet langsung dari URL sehingga perlu untuk download terlebih dahulu lalu dibaca. 
```python
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-05.parquet'
    file_name = url.split('/')[-1].replace('-', '_')
    print('Downloading File ({file_name}) .....')
    os.system(f"wget {url} -O {file_name}")

    df = pq.read_table(file_name).to_pandas()

    return df
```
Informasi mengenai data: 
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3723833 entries, 0 to 3723832
Data columns (total 19 columns):
 #   Column                 Dtype         
---  ------                 -----         
 0   VendorID               int32         
 1   tpep_pickup_datetime   datetime64[us]
 2   tpep_dropoff_datetime  datetime64[us]
 3   passenger_count        float64       
 4   trip_distance          float64       
 5   RatecodeID             float64       
 6   store_and_fwd_flag     object        
 7   PULocationID           int32         
 8   DOLocationID           int32         
 9   payment_type           int64         
 10  fare_amount            float64       
 11  extra                  float64       
 12  mta_tax                float64       
 13  tip_amount             float64       
 14  tolls_amount           float64       
 15  improvement_surcharge  float64       
 16  total_amount           float64       
 17  congestion_surcharge   float64       
 18  Airport_fee            float64       
dtypes: datetime64[us](2), float64(12), int32(3), int64(1), object(1)
memory usage: 497.2+ MB
```
#### Transform   
Dalam data ini, terdapat beberapa yang perlu dibersihkan atau Transform. Di antaranya: 
- Passengeer Count terdapat yang bernilai 0
- Trip Distance terdapat yang bernilai 0 
- Terdapat NaN data.

Sehingga perlu dihilang terlebih dahulu sebelum upload ke BigQuery. Kemudian, dilakukan data modelling menggunakan **star schema**. Anda bisa melihat codenya di sini: [transform_ny_taxi.py](https://github.com/MZakyFirdaus/Portofolio-Projects/blob/main/Projects/NY%20Taxi/mage-files/transformer/transfrom_ny_taxi.py)
```python
@transformer
def transform(df, *args, **kwargs):

    df = df[(df["passenger_count"] != 0) & (df["trip_distance"] != 0)]
    df.dropna(inplace=True)
    df = df.reset_index(drop=True)
    df["trip_id"] = df.index
    # ....
    # ....
    # ....
    return {
        "uber_trips_data_2024_5": df, 
        "vendor_dim": vendor_dim,
        "rate_code_dim": rate_code_dim,
        "payment_type_dim": payment_type_dim,
    }
```
#### Load
Tahap akhir dari ETL, upload file ke Google Big Query. 
Anda bisa lihat codenya di sini: [export_nytaxi_bq.py](https://github.com/MZakyFirdaus/Portofolio-Projects/blob/main/Projects/NY%20Taxi/mage-files/exporter/export_nytaxi_bq.py)
```python
@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    for table_name, df in data.items():
        table_id = f"<your_project>.<your_datasets>.{table_name}"
        config_path = path.join(get_repo_path(), "io_config.yaml")
        config_profile = "default"

        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            table_id,
            if_exists="replace",  # Specify resolution policy if table name already exists
        )
```
Cek Bigquery, dan anda bisa melihat dataset anda sudah terdapat di big query.   

![Bigquery Overview](/Projects/NY%20Taxi/img/bigquery_overview.png)

### Looker Studio
![Dashboard](/Projects/NY%20Taxi/img/Nyc_Yellow_Taxi_Dashboard.jpg)
