from pyspark.sql import SparkSession


def create_spark_session(
    app_name: str = "DiabetesAnalysis",
    master: str = "local[*]",
) -> SparkSession:
    """
    Create and return a SparkSession.

    Parameters
    ----------
    app_name : str
        Name of the Spark application.

    master : str
        Spark master URL.

    Returns
    -------
    SparkSession
    """

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master(master)
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark