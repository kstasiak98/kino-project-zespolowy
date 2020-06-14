# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bilet(models.Model):
    bilet_id = models.AutoField(db_column='BILET_ID', primary_key=True)  # Field name made lowercase.
    seans = models.ForeignKey('Seans', models.DO_NOTHING, db_column='SEANS_ID', blank=True)  # Field name made lowercase.
    cena = models.ForeignKey('Cennik', models.DO_NOTHING, db_column='CENA_ID')  # Field name made lowercase.
    rodzaj_biletu = models.CharField(db_column='RODZAJ_BILETU', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'BILET'


class Cennik(models.Model):
    cena_id = models.AutoField(db_column='CENA_ID', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='NAZWA', max_length=100)  # Field name made lowercase.
    cena = models.DecimalField(db_column='CENA', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        db_table = 'CENNIK'


class Film(models.Model):
    film_id = models.AutoField(db_column='FILM_ID', primary_key=True)  # Field name made lowercase.
    tytul = models.CharField(db_column='TYTUL', max_length=100)  # Field name made lowercase.
    czas_trwania = models.TimeField(db_column='CZAS_TRWANIA')  # Field name made lowercase.
    ocena = models.DecimalField(db_column='OCENA', max_digits=4, decimal_places=2, blank=True, null=True, default=0)  # Field name made lowercase.
    opis = models.TextField(db_column='OPIS')  # Field name made lowercase.

    class Meta:
        db_table = 'FILM'


class Klient(models.Model):
    klient_id = models.AutoField(db_column='KLIENT_ID', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='IMIE', max_length=100)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='NAZWISKO', max_length=100)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100)  # Field name made lowercase.
    haslo = models.CharField(db_column='HASLO', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'KLIENT'


class Produkt(models.Model):
    produkt_id = models.AutoField(db_column='PRODUKT_ID', primary_key=True)  # Field name made lowercase.
    cena_id = models.IntegerField(db_column='CENA_ID')  # Field name made lowercase.
    nazwa_produktu = models.CharField(db_column='NAZWA_PRODUKTU', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'PRODUKT'


class Sala(models.Model):
    sala_id = models.AutoField(db_column='SALA_ID', primary_key=True)  # Field name made lowercase.
    liczba_kolumn = models.IntegerField(db_column='LICZBA_KOLUMN')  # Field name made lowercase.
    liczba_rzedow = models.IntegerField(db_column='LICZBA_RZEDOW')  # Field name made lowercase.

    class Meta:
        db_table = 'SALA'


class Seans(models.Model):
    seans_id = models.AutoField(db_column='SEANS_ID', primary_key=True)  # Field name made lowercase.
    film = models.ForeignKey(Film, models.DO_NOTHING, db_column='FILM_ID')  # Field name made lowercase.
    sala = models.ForeignKey(Sala, models.DO_NOTHING, db_column='SALA_ID')  # Field name made lowercase.
    data = models.DateField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    godzina = models.TimeField(db_column='GODZINA')  # Field name made lowercase.

    class Meta:
        db_table = 'SEANS'


class ZajeteMiejsca(models.Model):
    miejsce_id = models.AutoField(db_column='MIEJSCE_ID', primary_key=True)  # Field name made lowercase.
    seans = models.ForeignKey(Seans, models.DO_NOTHING, db_column='SEANS_ID')  # Field name made lowercase.
    adres_miejsca = models.CharField(db_column='ADRES_MIEJSCA', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'ZAJETE_MIEJSCA'


class Zamowienie(models.Model):
    zamowienie_id = models.AutoField(db_column='ZAMOWIENIE_ID', primary_key=True)  # Field name made lowercase.
    klient = models.ForeignKey(Klient, models.DO_NOTHING, db_column='KLIENT_ID')  # Field name made lowercase.
    bilet = models.ForeignKey(Bilet, models.DO_NOTHING, db_column='BILET_ID', blank=True, null=True)  # Field name made lowercase.
    produkt = models.ForeignKey(Produkt, models.DO_NOTHING, db_column='PRODUKT_ID', blank=True, null=True)  # Field name made lowercase.
    do_zaplaty = models.DecimalField(db_column='DO_ZAPLATY', max_digits=4, decimal_places=2)  # Field name made lowercase.

    class Meta:
        db_table = 'ZAMOWIENIE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
