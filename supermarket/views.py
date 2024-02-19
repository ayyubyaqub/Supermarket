# categories->clothes,foods,jewelleries
# subcategories->clothes['shirts','jeans','coats','jacket'],foods['rice','vegetables','sweets'],jewelleries['gold','silver','platinum']
# item->clothes['shirts':{cotton,red},'jeans':{},'coats','jacket'],foods['rice','vegetables','sweets'],jewelleries['gold','silver','platinum']



from rest_framework import viewsets
from .models import Category, SubCategory, Item
from .serializers import CategorySerializer, SubCategorySerializer, ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer