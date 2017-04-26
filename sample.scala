import org.apache.spark._
import org.apache.spark.sql._

object sample extends App{
	val sc = new SparkContext()
	val spark = SparkSession.builder()
  				.appName("Spark SQL basic example")
  				.getOrCreate()

  	val reviewsDF = spark.read.format("json").load("/home/nir0303/independentstudy/yelp_academic_dataset_review.json")			
  	
  	val limitDF = reviewsDF.limit(10000)
  	limitDF.createOrReplaceTempView("reviews")
  	val businessDF = spark.read.format("json").load("/home/nir0303/independentstudy/yelp_academic_dataset_business.json")
  	businessDF.createOrReplaceTempView("business")
  	val restautrantsDF= spark.sql("select b.* from business b join reviews r on b.business_id = r.business_id")
  	restautrantsDF.repartition(1).write.format("json").save("data/restautrants/")
  	limitDF.write.format("json").save("data/reviews100000/")


}