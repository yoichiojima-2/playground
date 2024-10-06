from pyspark.sql import DataFrame


# start spark session
def start_spark():
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("example-pyspark").getOrCreate()
    return spark


def create_data() -> DataFrame:
    """
    >>> df = create_data().printSchema() # doctest: +NORMALIZE_WHITESPACE
    root
    |-- age: long (nullable = true)
    |-- name: string (nullable = true)
    """
    spark = start_spark()
    data = [
        {"name": "Alice", "age": 34},
        {"name": "Bob", "age": 45},
        {"name": "Charlie", "age": 45},
    ]
    return spark.createDataFrame(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
