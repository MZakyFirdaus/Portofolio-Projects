import pandas as pd

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = df[(df["passenger_count"] != 0) & (df["trip_distance"] != 0)]
    df.dropna(inplace=True)
    df = df.reset_index(drop=True)
    df["trip_id"] = df.index

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

    # Create Vendor Dimension
    vendor_dim = df[['VendorID']].drop_duplicates().reset_index(drop=True)

    mapping = {
        1: "Creative Mobile Technologies, LLC",
        2: "VeriFone Inc."
    }

    vendor_dim['vendor_provider'] = vendor_dim['VendorID'].map(mapping)
    vendor_dim = vendor_dim[['VendorID', 'vendor_provider']]

    # Create RatecodeID Dimensional table
    rate_code_dim = df[['RatecodeID']].drop_duplicates().reset_index(drop=True)
    mapping = {
        1: "Standard Rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride"
    }
    rate_code_dim['rate_code_type'] = rate_code_dim['RatecodeID'].map(mapping)
    rate_code_dim = rate_code_dim[['RatecodeID', 'rate_code_type']]

    # Create Payment type Dimensional table
    payment_type_dim = df[['payment_type']].drop_duplicates().reset_index(drop=True)

    mapping = {
        1: 'Credit card',
        2: 'Cash',
        3: 'No charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided trip'
    }

    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(mapping)
    payment_type_dim = payment_type_dim[['payment_type', 'payment_type_name']]
    return {
        "uber_trips_data_2024_5": df, 
        "vendor_dim": vendor_dim,
        "rate_code_dim": rate_code_dim,
        "payment_type_dim": payment_type_dim,
    }
