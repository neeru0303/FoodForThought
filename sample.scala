import org.apache.spark._
import org.apache.spark.sql._

object sample extends App{
	val sc = new SparkContext()
	val spark = SparkSession.builder()
  				.appName("Spark SQL basic example")
  				.getOrCreate()

  	val reviewsDf = spark.read.format("json").load("/home/nir0303/independentstudy/yelp_academic_dataset_review.json")			
  	println(reviewsDf.printSchema())
  	val limitDf = reviewsDf.limit(10000)

  	limitDf.write.format("json").save("data/reviews100000/")


}