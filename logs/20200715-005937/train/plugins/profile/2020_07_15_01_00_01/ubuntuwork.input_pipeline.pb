	Rd��t}�@Rd��t}�@!Rd��t}�@	�=fG:p�?�=fG:p�?!�=fG:p�?"h
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails'�*Rd��t}�@�e���@A�|�͍f@Y[��vNzR@*33333��@g��|wF�@2o
8Iterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::MapdO���N;R@!mYS*�S@)��	�_�Q@1���sS@:Preprocessing2�
eIterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMap::ParallelMapeg{�&@!��^���(@)g{�&@1��^���(@:Preprocessing2�
XIterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMapd��A�g@!��J#@)��A�g@1��J#@:Preprocessing2x
AIterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffled�U�0���?!��h� �?)Yk(��?1��Ml�?:Preprocessing2�
KIterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetchd R�8���?!��9����?) R�8���?1��9����?:Preprocessing2�
�Iterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMap::ParallelMap::AssertCardinality::ParallelInterleaveV3[0]::FlatMap[0]::TFRecordeI.�!���?!�tߍ���?)I.�!���?1�tߍ���?:Advanced file read2�
�Iterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMap::ParallelMap::AssertCardinality::ParallelInterleaveV3e��&2s�?!Y�D3io�?)��&2s�?1Y�D3io�?:Preprocessing2U
Iterator::Model::PaddedBatchV2��RbxR@!���K�T@)�E����?1��#��?:Preprocessing2�
xIterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMap::ParallelMap::AssertCardinalitye\1е/�?!�ҍ��p�?)E�<�\�?1Ё�'���?:Preprocessing2^
'Iterator::Model::PaddedBatchV2::ShuffledL�g�[R@!�	xh��S@)\�����?1�)�8��?:Preprocessing2�
�Iterator::Model::PaddedBatchV2::Shuffle::FiniteSkip::Map::Shuffle::Prefetch::ParallelMap::ParallelMap::AssertCardinality::ParallelInterleaveV3[0]::FlatMape�8�ߡ��?!+��q+
�?)�t{Ic�?1� %����?:Preprocessing2j
3Iterator::Model::PaddedBatchV2::Shuffle::FiniteSkipd����ER@!�j0��S@)��pz�?1�/�����?:Preprocessing2F
Iterator::Model����xR@!��5!�T@)��A{��p?1f��fur?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 1.1% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B96.3 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	�e���@�e���@!�e���@      ��!       "      ��!       *      ��!       2	�|�͍f@�|�͍f@!�|�͍f@:      ��!       B      ��!       J	[��vNzR@[��vNzR@![��vNzR@R      ��!       Z	[��vNzR@[��vNzR@![��vNzR@JCPU_ONLY