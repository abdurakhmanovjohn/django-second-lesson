from django.db import models

class Categories(models.Model):
  category_name = models.CharField(max_length=15)
  description = models.TextField(blank=True)
  picture = models.ImageField(upload_to='photos/%Y/%m/%d')

  def __str__(self):
    return self.category_name


class Customers(models.Model):
  company_name = models.CharField(max_length=40)
  contact_name = models.CharField(max_length=30)
  contact_title = models.CharField(max_length=30)
  address = models.CharField(max_length=60)
  city = models.CharField(max_length=15)
  region = models.CharField(max_length=15)
  postal_code = models.CharField(max_length=15)
  phone = models.CharField(max_length=24)
  fax = models.CharField(max_length=24)

  def __str__(self):
    return self.company_name


class Suppliers(models.Model):
  company_name = models.CharField(max_length=40)
  contact_name = models.CharField(max_length=30)
  contact_title = models.CharField(max_length=30)
  address = models.CharField(max_length=60)
  city = models.CharField(max_length=15)
  region = models.CharField(max_length=15)
  postal_code = models.CharField(max_length=15)
  phone = models.CharField(max_length=24)
  fax = models.CharField(max_length=24)
  homepage = models.TextField(blank=True)

  def __str__(self):
    return self.company_name


class Products(models.Model):
  product_name = models.CharField(max_length=40)
  supllier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
  category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
  quantity_per_unit = models.CharField(max_length=20)
  unit_price = models.FloatField()
  units_in_stock = models.SmallIntegerField()
  units_on_order = models.SmallIntegerField()
  reorder_level = models.SmallIntegerField()
  discontinued = models.IntegerField()

  def __str__(self):
    return self.product_name


# yozish hamda 5 tadan ma'lumot qo'shamiz .
# 3 chi ma'lumotni o'chirib 4-chisini upadte qilib kelish hamda skrenshotlarni yuklash.

# supplier_ids => 1, 2, 4, 5
# category_ids => 1, 2, 4, 5