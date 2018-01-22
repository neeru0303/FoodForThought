#!/usr/bin/env python2.7
import os
import logging

from pyspark.sql import *
from pyspark import *

BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH, "data/dataset")
RESTAURANT_REVIEWS_FILE = os.path.join(DATA_PATH, "review.json")
RESTAURANT_BUSINESS_FILE = os.path.join(DATA_PATH, "business.json")


def process():
    """
    driver program to generate restaurant reviews data
    :return:
    """
    sc = SparkContext()
    spark = SparkSession.Builder().appName("Spark SQL basic example").getOrCreate()

    logger.info("Read reviews data")
    review_df = spark.read.format("json").load("file:///"+RESTAURANT_REVIEWS_FILE)

    logger.info("Read business data")
    business_df = spark.read.format("json").load("file:///"+RESTAURANT_BUSINESS_FILE)
    review_df.createOrReplaceTempView("reviews")
    business_df.createOrReplaceTempView("business")

    #review_df.persist()
    #business_df.persist()

    logger.info("Get restaurant business data")
    restaurant_df = spark.sql("select distinct b1.* from (select business_id,new_column from business b1 "
                              "lateral view explode(categories) exploded_table as new_column) x,business b1 "
                              "where x.business_id = b1.business_id and new_column in ('Food','Restaurants')")

    restaurant_df.createOrReplaceTempView("restaurants")

    logger.info("Get restaurant business review data")
    restaurant_reviews_df = spark.sql("select distinct r_b.* from restaurants r_b "
                                      "join reviews r on r_b.business_id = r.business_id").limit(1000)

    logger.info("Save restaurant business review data")
    restaurant_reviews_df.repartition(1).write.format("json").save(os.path.join("file:///"+ DATA_PATH, "reviews_output"))

    #review_df.unpersist()
    #business_df.unpersist()

    spark.stop()


if __name__ == "__main__":
    logger = logging.getLogger("generate_data")
    file_handler = logging.FileHandler("logs/generate_data.log", mode="w")
    format_handler = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(format_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    try:
        logger.info("Start generate data")
        process()
    except Exception as err:
        logger.error("Process failed because of error {}".format(err))

