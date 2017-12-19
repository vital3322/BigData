find 95% interval

copy all files to docker root and run 'bash run.sh'


run:


1) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample/ -output sample_output/count -mapper map_count.py  -reducer reduce_count.py -file /map_count.py -file /reduce_count.py


2) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/count/ -output sample_output/mean -mapper map_mean.py  -reducer reduce_mean.py -file /map_mean.py -file /reduce_mean.py


3) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/count -input sample_output/mean -output sample_output/prepare_std -mapper map_prepare_std.py  -reducer reduce_prepare_std.py -file /map_prepare_std.py -file /reduce_prepare_std.py


4) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/prepare_std -output sample_output/std -mapper map_std.py  -reducer reduce_std.py -file /map_std.py -file /reduce_std.py


5) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/std -input sample_output/mean -input sample_output/count -output sample_output/interval -mapper map_interval.py  -reducer reduce_interval.py -file /map_interval.py -file /reduce_interval.py


6) bin/hadoop dfs -text sample_output/interval/*


=======================

clear:


1) bin/hadoop dfs -rmr sample_output/count
2) bin/hadoop dfs -rmr sample_output/mean
3) bin/hadoop dfs -rmr sample_output/prepare_std
4) bin/hadoop dfs -rmr sample_output/std
5) bin/hadoop dfs -rmr sample_output/interval
