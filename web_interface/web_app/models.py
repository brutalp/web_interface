# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actuator(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    slotcount = models.IntegerField(db_column='SlotCount')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actuator'


class Amplitudedistribution(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmplitudeDistribution'


class Analyticalline(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    atomicnumber = models.ForeignKey('Chemicalelement', models.DO_NOTHING, db_column='AtomicNumber')  # Field name made lowercase.
    emissionlineid = models.ForeignKey('Emissionline', models.DO_NOTHING, db_column='EmissionLineId', blank=True, null=True)  # Field name made lowercase.
    energy = models.FloatField(db_column='Energy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnalyticalLine'


class Basesetup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseSetup'


class Calendar(models.Model):
    idCalendar = models.IntegerField(db_column='Id')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar'


class Channelsetup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    setupinfoid = models.ForeignKey('Setupinfo', models.DO_NOTHING, db_column='SetupInfoId')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    channelnumber = models.SmallIntegerField(db_column='ChannelNumber')  # Field name made lowercase.
    lolevel = models.FloatField(db_column='LoLevel')  # Field name made lowercase.
    window = models.FloatField(db_column='Window')  # Field name made lowercase.
    gain = models.FloatField(db_column='Gain')  # Field name made lowercase.
    voltage = models.FloatField(db_column='Voltage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChannelSetup'


class Chemicalelement(models.Model):
    atomicnumber = models.SmallIntegerField(db_column='AtomicNumber', primary_key=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', unique=True, max_length=5)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    familyid = models.ForeignKey('Chemicalelementsfamily', models.DO_NOTHING, db_column='FamilyId', blank=True, null=True)  # Field name made lowercase.
    period = models.SmallIntegerField(db_column='Period', blank=True, null=True)  # Field name made lowercase.
    group = models.SmallIntegerField(db_column='Group', blank=True, null=True)  # Field name made lowercase.
    atomicmass = models.FloatField(db_column='AtomicMass', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    boilingpoint = models.FloatField(db_column='BoilingPoint', blank=True, null=True)  # Field name made lowercase.
    meltingpoint = models.FloatField(db_column='MeltingPoint', blank=True, null=True)  # Field name made lowercase.
    electronegativityallredandrochov = models.FloatField(db_column='ElectronegativityAllredAndRochov', blank=True, null=True)  # Field name made lowercase.
    electronegativitypauling = models.FloatField(db_column='ElectronegativityPauling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChemicalElement'


class Chemicalelementsfamily(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChemicalElementsFamily'


class Correction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    typeid = models.ForeignKey('Correctiontype', models.DO_NOTHING, db_column='TypeId')  # Field name made lowercase.
    quantityid = models.ForeignKey('Quantity', models.DO_NOTHING, db_column='QuantityId')  # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Correction'


class Correctiontype(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CorrectionType'


class Criterion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='ObjectId')  # Field name made lowercase.
    quantityid = models.ForeignKey('Quantity', models.DO_NOTHING, db_column='QuantityId')  # Field name made lowercase.
    typeid = models.ForeignKey('Criteriontype', models.DO_NOTHING, db_column='TypeId')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Criterion'


class Criteriontype(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CriterionType'


class Cycle(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    doubleloop = models.BooleanField(db_column='DoubleLoop')  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    uniform = models.BooleanField(db_column='Uniform')  # Field name made lowercase.
    maxmovementtime = models.IntegerField(db_column='MaxMovementTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cycle'


class Emissionline(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmissionLine'


class Event(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    sourceid = models.ForeignKey('Eventsource', models.DO_NOTHING, db_column='SourceId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.TextField(db_column='OldValue', blank=True, null=True)  # Field name made lowercase.
    newvalue = models.TextField(db_column='NewValue', blank=True, null=True)  # Field name made lowercase.
    emergency = models.BooleanField(db_column='Emergency')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event'


class Eventsource(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventSource'


class Measurement(models.Model):
    unused = models.BooleanField(db_column='Unused')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    measurementtypeid = models.ForeignKey('Measurementtype',  models.DO_NOTHING, db_column='MeasurementTypeId', related_name='measurementTypeId')  # Field name made lowercase.
    methodobjectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='MethodObjectId', blank=True, null=True, related_name='methodObjectId')  # Field name made lowercase.
    sampleobjectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='SampleObjectId', blank=True, null=True, related_name='sampleObjectId')  # Field name made lowercase.
    parentmeasurementid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentMeasurementId', blank=True, null=True, related_name='parentMeasurementId')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid', blank=True, null=True)  # Field name made lowercase.
    shiftnumber = models.IntegerField(db_column='ShiftNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Measurement'


class Measurementdatamap(models.Model):
    id = models.AutoField(db_column='Id', unique=True, primary_key=True)  # Field name made lowercase.
    measurementid = models.OneToOneField(Measurement, models.DO_NOTHING, db_column='MeasurementId')  # Field name made lowercase.
    dataobjectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='DataObjectId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementDataMap'
        unique_together = (('measurementid', 'dataobjectid'),)


class Measurementtype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementType'


class Metainfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    strvalue = models.TextField(db_column='StrValue', blank=True, null=True)  # Field name made lowercase.
    intvalue = models.IntegerField(db_column='IntValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MetaInfo'


class Modbus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    pinginterval = models.IntegerField(db_column='PingInterval', blank=True, null=True)  # Field name made lowercase.
    connecttype = models.TextField(db_column='ConnectType', blank=True, null=True)  # Field name made lowercase.
    tcpaddress = models.TextField(db_column='TCPAddress', blank=True, null=True)  # Field name made lowercase.
    tcpport = models.IntegerField(db_column='TCPPort', blank=True, null=True)  # Field name made lowercase.
    rtuport = models.TextField(db_column='RTUPort', blank=True, null=True)  # Field name made lowercase.
    rtuspeed = models.IntegerField(db_column='RTUSpeed', blank=True, null=True)  # Field name made lowercase.
    rtuparity = models.TextField(db_column='RTUParity', blank=True, null=True)  # Field name made lowercase.
    rtustartbits = models.IntegerField(db_column='RTUStartBits', blank=True, null=True)  # Field name made lowercase.
    rtustopbits = models.IntegerField(db_column='RTUStopBits', blank=True, null=True)  # Field name made lowercase.
    rtumodbusaddress = models.IntegerField(db_column='RTUModbusAddress', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modbus'


class Object(models.Model):
    unused = models.BooleanField(db_column='Unused')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objecttypeid = models.IntegerField(db_column='ObjectTypeId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    creationtimestamp = models.DateTimeField(db_column='CreationTimestamp')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    parentobjectid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentObjectId', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Object'


class Objectgroup(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectGroup'


class Objectgroupobject(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objectid = models.ForeignKey(Object, models.DO_NOTHING, db_column='ObjectId')  # Field name made lowercase.
    groupid = models.ForeignKey(Objectgroup, models.DO_NOTHING, db_column='GroupId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectGroupObject'


class Objectquantitymap(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objectid = models.ForeignKey(Object, models.DO_NOTHING, db_column='ObjectId', blank=True, null=True)  # Field name made lowercase.
    quantityid = models.ForeignKey('Quantity', models.DO_NOTHING, db_column='QuantityId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectQuantityMap'
        unique_together = (('objectid', 'quantityid'),)


class Objecttype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.
    supertypeid = models.ForeignKey('self', models.DO_NOTHING, db_column='SuperTypeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectType'


class Pointparameter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectId', blank=True, null=True)  # Field name made lowercase.
    secondloop = models.BooleanField(db_column='SecondLoop')  # Field name made lowercase.
    slotnumber = models.IntegerField(db_column='SlotNumber', blank=True, null=True)  # Field name made lowercase.
    pointnumber = models.IntegerField(db_column='PointNumber', blank=True, null=True)  # Field name made lowercase.
    cutoffduration = models.IntegerField(db_column='CutOffDuration', blank=True, null=True)  # Field name made lowercase.
    timebeforeanalytic = models.TimeField(db_column='TimeBeforeAnalytic', blank=True, null=True)  # Field name made lowercase.
    pulppumpingduration = models.TimeField(db_column='PulpPumpingDuration', blank=True, null=True)  # Field name made lowercase.
    washingduration = models.TimeField(db_column='WashingDuration', blank=True, null=True)  # Field name made lowercase.
    cutoffdelay = models.TimeField(db_column='CutOffDelay', blank=True, null=True)  # Field name made lowercase.
    pumppulse = models.FloatField(db_column='PumpPulse', blank=True, null=True)  # Field name made lowercase.
    pumppulsepause = models.FloatField(db_column='PumpPulsePause', blank=True, null=True)  # Field name made lowercase.
    washingdurationwm = models.TimeField(db_column='WashingDurationWM', blank=True, null=True)  # Field name made lowercase.
    pausedurationwm = models.TimeField(db_column='PauseDurationWM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointParameter'


class Programproductdependence(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    programguid = models.UUIDField(db_column='ProgramGuid')  # Field name made lowercase.
    productguid = models.UUIDField(db_column='ProductGuid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgramProductDependence'
        unique_together = (('programguid', 'productguid'),)


class Property(models.Model):
    key = models.TextField(db_column='Key', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Property'


class Quantity(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    typeid = models.ForeignKey('Quantitytype', models.DO_NOTHING, db_column='TypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quantity'
        unique_together = (('name', 'typeid'),)


class Quantitygroup(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='UnitId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityGroup'
        unique_together = (('name', 'unitid'),)


class Quantitytype(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityType'


class Setupinfo(models.Model):
    unused = models.BooleanField(db_column='Unused')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SetupInfo'


class Slot(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    actuatorid = models.ForeignKey(Actuator, models.DO_NOTHING, db_column='ActuatorId')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    group = models.IntegerField(db_column='Group')  # Field name made lowercase.
    exposure = models.IntegerField(db_column='Exposure')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Slot'


class Sourcetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SourceType'


class Transitionmatrix(models.Model):
    unused = models.BooleanField(db_column='Unused')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    exposure = models.FloatField(db_column='Exposure')  # Field name made lowercase.
    meascount = models.SmallIntegerField(db_column='MeasCount')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    data = models.BinaryField(db_column='Data')  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransitionMatrix'


class Unit(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    shortname = models.TextField(db_column='ShortName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unit'
        unique_together = (('name', 'shortname'),)


class Unusable(models.Model):
    unused = models.BooleanField(db_column='Unused')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unusable'


class Userinfo(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    dbid = models.IntegerField(db_column='DbId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'


class Value(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.
    quantityid = models.ForeignKey(Quantity, models.DO_NOTHING, db_column='QuantityId')  # Field name made lowercase.
    quantitygroupid = models.ForeignKey(Quantitygroup, models.DO_NOTHING, db_column='QuantityGroupId')  # Field name made lowercase.
    sourcetypeid = models.ForeignKey(Sourcetype, models.DO_NOTHING, db_column='SourceTypeId')  # Field name made lowercase.
    multiplicity = models.SmallIntegerField(db_column='Multiplicity', blank=True, null=True)  # Field name made lowercase.
    absoluteerror = models.FloatField(db_column='AbsoluteError', blank=True, null=True)  # Field name made lowercase.
    measurementid = models.ForeignKey(Measurement, models.DO_NOTHING, db_column='MeasurementId')  # Field name made lowercase.
    exposure = models.FloatField(db_column='Exposure', blank=True, null=True)  # Field name made lowercase.
    criteria = models.IntegerField(db_column='Criteria', blank=True, null=True)  # Field name made lowercase.
    setupid = models.IntegerField(db_column='SetupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Value'


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
