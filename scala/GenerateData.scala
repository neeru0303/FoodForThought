import org.apache.spark._
import org.apache.spark.sql._

object GenerateData extends App{
	val sc = new SparkContext()
	val spark = SparkSession.builder()
  				.appName("Restaurant Data Cleanse")
  				.getOrCreate()

  	val reviewsDF = spark.read.format("json").load("/home/nir0303/independentstudy/yelp_academic_dataset_review.json")			
  	
  	//val limitDF = reviewsDF.limit(10000)
  	reviewsDF.createOrReplaceTempView("reviews")
  	reviewsDF.persist()
  	val businessDF = spark.read.format("json").load("/home/nir0303/independentstudy/yelp_academic_dataset_business.json")
  	businessDF.persit
  	businessDF.createOrReplaceTempView("restaurant")
    val rest = spark.sql("select distinct r1.* from (select business_id,new_column from restaurant r1 lateral view explode(categories) exploded_table as new_column) x,restaurant r1 where x.business_id = r1.business_id and new_column in ('Food','Restaurants')")
    rest.createOrReplaceTempView("business")
  	val restautrantsDF= spark.sql("select distinct b.* from business b join reviews r on b.business_id = r.business_id")
  	restautrantsDF.repartition(1).write.format("json").save("data/restautrants/")
  	val newreviewsDF = spark.sql("select distinct r.* from reviews r join business b on r.business_id = b.business_id").limit(100000)
    newreviewsDF.write.format("json").save("data/reviews100000/")


}

