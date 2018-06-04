# Generated by Django 2.0.5 on 2018-05-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=10, verbose_name='商品编号')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名称')),
                ('goods_type', models.CharField(max_length=10, verbose_name='商品类别')),
                ('plan_in_cost', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='计划进货价格')),
                ('plan_out_cost', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='计划出货价格')),
                ('storage', models.IntegerField(verbose_name='原始库存')),
            ],
        ),
        migrations.CreateModel(
            name='inStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_id', models.CharField(max_length=10, verbose_name='入库单号')),
                ('in_date', models.DateField(verbose_name='入库日期')),
                ('goods_id', models.CharField(max_length=10, verbose_name='商品编号')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名称')),
                ('in_number', models.IntegerField(verbose_name='进货数量')),
                ('in_cost', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='进货价格')),
                ('in_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='进货总价')),
            ],
        ),
        migrations.CreateModel(
            name='outStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_id', models.CharField(max_length=10, verbose_name='出库单号')),
                ('out_date', models.DateField(verbose_name='出库日期')),
                ('goods_id', models.CharField(max_length=10, verbose_name='商品编号')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名称')),
                ('out_number', models.IntegerField(verbose_name='出货数量')),
                ('out_cost', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='出货价格')),
                ('out_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='出货总价')),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=10, verbose_name='商品编号')),
                ('goods_name', models.CharField(max_length=10, verbose_name='商品名称')),
                ('last_month', models.CharField(max_length=10, verbose_name='上月盘存')),
                ('inNum', models.CharField(max_length=10, verbose_name='本月入库')),
                ('outNum', models.CharField(max_length=10, verbose_name='本月出库')),
                ('remain', models.CharField(max_length=10, verbose_name='结余')),
                ('profit', models.CharField(max_length=10, verbose_name='盈亏数量')),
            ],
        ),
    ]