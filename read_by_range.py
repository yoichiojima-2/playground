from datetime import date
from dataclasses import dataclass

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


spark: SparkSession = SparkSession.builder.getOrCreate()


@dataclass
class S3Client:
    available_path: list[str]
    unavailable_path: list[str]

    def check_exsistance_by_range(self, start_date: date, end_date: date) -> bool: ...


@dataclass
class ParquetReader:
    s3_client: S3Client
    path: str

    def read_by_range(self, start_date: date, end_date: date) -> DataFrame:
        self.s3_client.check_exsistance_by_range(start_date, end_date)
        return spark.read.set_option("basePath", self.path).parquet(
            self.s3_client.available_path
        )
