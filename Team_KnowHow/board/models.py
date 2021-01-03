from django.db import models

class CBCodeHdr(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    type_nm = models.CharField(db_column='type_nm', max_length=50)
    type_nmen = models.CharField(db_column='type_nmen', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt')
    insrt_dt = models.DateTimeField(db_column='insrt_dt')
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt_id = models.IntegerField(db_column='insrt_id')
    updt_id = models.IntegerField(db_column='updt_id')

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'

    def __str__(self):
        return "Code type : " + self.type_nm

class CBCodeDtl(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    type_cd = models.CharField(db_column='type_cd', max_length=20)
    code_cd = models.CharField(db_column='code_cd', max_length=20)
    cd_nm = models.CharField(db_column='cd_nm', max_length=50)
    cd_nmen = models.CharField(db_column='cd_nmen', max_length=50)
    updt_dt = models.DateTimeField(db_column='updt_dt')
    insrt_dt = models.DateTimeField(db_column='insrt_dt')
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, default='Y')
    insrt_id = models.IntegerField(db_column='insrt_id')
    updt_id = models.IntegerField(db_column='updt_id')

    class Meta:
        managed = False
        db_table = 'cb_code_hdr'

    def __str__(self):
        return "Code type : " + self.cd_nm