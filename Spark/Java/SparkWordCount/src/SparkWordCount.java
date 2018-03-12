import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import scala.Tuple2;

import java.util.Arrays;

public class SparkWordCount {
    public static void main(String[] args) {
        String inputFile = args[0];
        SparkConf sparkConf = new SparkConf().setMaster("local").setAppName("WordCount");
        JavaSparkContext sc = new JavaSparkContext(sparkConf);
        JavaRDD<String> textFile = sc.textFile(inputFile);
        JavaRDD<String> words = textFile.flatMap(
                new FlatMapFunction<String, String>() {
                    public Iterable<String> call(String x) {
                        return Arrays.asList(x.split(" "));
                    }
                }
        );
        JavaPairRDD<String, Integer> counts = words.mapToPair(
                new PairFunction<String, String, Integer>() {
                    public Tuple2<String, Integer> call(String x) {
                        return new Tuple2(x, 1);
                    }
                }
        ).reduceByKey(new Function2<Integer, Integer, Integer>(){
            public Integer call(Integer x, Integer y) {
                return x + y;
            }
        });
        System.out.println(counts.collect());
    }

}