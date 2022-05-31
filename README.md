# Hugging Face object detection plugin for scivision

Model repository for the [scivision](https://scivision.readthedocs.io/) project that enables loading of object detection models from [Hugging Face](https://huggingface.co/models?pipeline_tag=object-detection&sort=downloads).

Via the scivision API, the [top 10 downloaded Image Classification models from Hugging Face](https://huggingface.co/models?pipeline_tag=object-detection&sort=downloads) (of models with a model card, last updated 31st May 2022) can be installed, loaded and run. The list of models is as follows:

1. [facebook_detr_resnet_50](https://huggingface.co/facebook/detr-resnet-50)
2. [hustvl_yolos_small](https://huggingface.co/hustvl/yolos-small)
3. [detr_doc_table_detection](https://huggingface.co/TahaDouaji/detr-doc-table-detection)
4. [detr_resnet_101](https://huggingface.co/facebook/detr-resnet-101)

Models in this list can be loaded and used on data with a few lines of code, e.g.

```python
from scivision import load_pretrained_model
this_repo = 'https://github.com/alan-turing-institute/scivision_huggingface_objectdetection'
model = load_pretrained_model(this_repo, model='facebook_detr_resnet_50')
```

You can then use the loaded model's predict function on image data loaded via *scivision* (see the [user guide](https://scivision.readthedocs.io/en/latest/user_guide.html) for details on how data is loaded via the scivision catalog):

```python
model.predict(<image data>)
```
