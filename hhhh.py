# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=200)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Equipment'


class Unit(models.Model):
    id_unitgroup = models.ForeignKey('Untigroup', models.DO_NOTHING, db_column='id_unitGroup')  # Field name made lowercase.
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    time = models.DecimalField(max_digits=18, decimal_places=0)
    periodicity = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    executor = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Unit'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodesTest(models.Model):
    barcode_1 = models.CharField(max_length=50, blank=True, null=True)
    barcode_2 = models.CharField(max_length=50, blank=True, null=True)
    barcode_3 = models.CharField(max_length=50, blank=True, null=True)
    barcode_4 = models.CharField(max_length=50, blank=True, null=True)
    barcode_5 = models.CharField(max_length=50, blank=True, null=True)
    barcode_6 = models.CharField(max_length=50, blank=True, null=True)
    barcode_7 = models.CharField(max_length=50, blank=True, null=True)
    barcode_8 = models.CharField(max_length=50, blank=True, null=True)
    barcode_9 = models.CharField(max_length=50, blank=True, null=True)
    barcode_10 = models.CharField(max_length=50, blank=True, null=True)
    barcode_11 = models.CharField(max_length=50, blank=True, null=True)
    barcode_12 = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    board_number = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcodes_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EquipmentEquip(models.Model):
    inv_number = models.CharField(max_length=100)
    equipment_id = models.ForeignKey(Equipment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'equipment_equip'


class EquipmentEquipUnits(models.Model):
    equip = models.ForeignKey(EquipmentEquip, models.DO_NOTHING)
    unit = models.ForeignKey(Unit, models.DO_NOTHING)
    fact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_equip_units'
        unique_together = (('equip', 'unit'),)


class EquipmentMaintenance(models.Model):
    actual_quantity = models.DecimalField(max_digits=18, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'equipment_maintenance'


class Maintenance(models.Model):
    id_equip = models.DecimalField(max_digits=18, decimal_places=0)
    actual_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenance'


class Untigroup(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'untiGroup'


class UpackJournalTest(models.Model):
    kb_num = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    row_number = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    type_of_pack = models.CharField(max_length=50, blank=True, null=True)
    position_kb = models.CharField(max_length=50, blank=True, null=True)
    fio_upack = models.CharField(max_length=50, blank=True, null=True)
    upak_list_number = models.IntegerField(blank=True, null=True)
    autocarrier = models.CharField(max_length=100, blank=True, null=True)
    recipient = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    order_num = models.CharField(max_length=50, blank=True, null=True)
    qty_formed = models.DecimalField(max_digits=19, decimal_places=8, blank=True, null=True)
    sel_kb_pos = models.TextField(blank=True, null=True)
    temp = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upack_journal_test'


class Work(models.Model):
    id_user = models.IntegerField()
    id_maintaince = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'work'
