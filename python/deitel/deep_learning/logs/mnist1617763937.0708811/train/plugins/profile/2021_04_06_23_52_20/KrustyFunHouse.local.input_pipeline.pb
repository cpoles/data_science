	h��|?EG@h��|?EG@!h��|?EG@	��/_�?��/_�?!��/_�?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$h��|?EG@+����?A�� �r�F@Y����K�?*	     ��@2U
Iterator::Model::ParallelMapV21�Zd�?!��S��J@)1�Zd�?1��S��J@:Preprocessing2F
Iterator::Model=
ףp=�?!Ap8�)U@)J+��?1��w�B@@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate�Q���?!>uh!@)�������?1�4L\@:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice{�G�z�?!���	}@){�G�z�?1���	}@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor;�O��n�?!EڴL"�@);�O��n�?1EڴL"�@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::ZipT㥛� �?!�}<��.@)�� �rh�?1�?ǝ�� @:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat�� �rh�?!�?ǝ��@)����Mb�?1%K��u.�?:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap333333�?!�9E"@){�G�zt?1���	}�?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 1.6% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9��/_�?I�@���X@Zno#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	+����?+����?!+����?      ��!       "      ��!       *      ��!       2	�� �r�F@�� �r�F@!�� �r�F@:      ��!       B      ��!       J	����K�?����K�?!����K�?R      ��!       Z	����K�?����K�?!����K�?b      ��!       JCPU_ONLYY��/_�?b q�@���X@