from os import path

from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from mage_ai.settings.repo import get_repo_path
from pandas import DataFrame

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    for table_name, df in data.items():
        table_id = f"firdauszakyy-de.yellow_trips_data.{table_name}"
        config_path = path.join(get_repo_path(), "io_config.yaml")
        config_profile = "default"

        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            table_id,
            if_exists="replace",  # Specify resolution policy if table name already exists
        )