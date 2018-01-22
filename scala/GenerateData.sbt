name := "sample"

version := "0.0.1"

scalaVersion := "2.11.8"

// additional libraries
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "2.1.0" % "provided",
  "org.apache.spark" %% "spark-sql" % "2.1.0",
  "org.apache.spark" %% "spark-streaming" % "2.1.0"
)