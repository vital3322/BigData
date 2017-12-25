Упростили 1-ю задачу:
Берем данные из файла и для каждого значение antiNucleus высчитываете СРЕДНЕЕ prodTime
Далее берете только те строки, у которых prodTime выше СРЕДНЕГО для соответствующего ему antiNucleus
В итоге для каждого antiNucleus для отобранных значений высчитать количество уникальных eventFile и среднее значение Pt


create docker and copy files:
0) docker pull sequenceiq/hadoop-docker:2.7.1
1) docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash
2) docker cp sample.csv MY_NAME:/sample.csv
3) docker cp map0.py MY_NAME:/map0.py
4) docker cp reduce0.py MY_NAME:/reduce0.py

create files in docker:
0) cd $HADOOP_PREFIX
1) bin/hdfs dfs -mkdir sample
2) bin/hdfs dfs -put файл папка_в_хдфс

run map-reduce tasks on docker:

0) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample/ -output sample_output/selectdata -mapper map0.py  -reducer reduce0.py -file /map0.py -file /reduce0.py
1) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/selectdata -output sample_output/mean -mapper map1.py  -reducer reduce1.py -file /map1.py -file /reduce1.py
2) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/selectdata -input sample_output/mean -output sample_output/prepare_prodtime -mapper map2.py  -reducer reduce2.py -file /map2.py -file /reduce2.py
3) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/prepare_prodtime -output sample_output/prodtime -mapper map3.py  -reducer reduce3.py -file /map3.py -file /reduce3.py
4) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/prodtime -output sample_output/eventfile -mapper map4.py  -reducer reduce4.py -file /map4.py -file /reduce4.py
5) bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input sample_output/prodtime -output sample_output/pt -mapper map5.py  -reducer reduce5.py -file /map5.py -file /reduce5.py

show results:
7) bin/hdfs dfs -text sample_output/eventfile/*
6) bin/hdfs dfs -text sample_output/pt/*
=======================

clear:


1) bin/hadoop dfs -rmr sample_output/selectdata
2) bin/hadoop dfs -rmr sample_output/mean
3) bin/hadoop dfs -rmr sample_output/prodtime
4) bin/hadoop dfs -rmr sample_output/eventfile
5) bin/hadoop dfs -rmr sample_output/pt
