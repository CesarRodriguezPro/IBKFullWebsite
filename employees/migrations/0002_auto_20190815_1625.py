# Generated by Django 2.2.3 on 2019-08-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='licenses',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='status',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='warningnotices',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='workerscompensation',
            name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='ACI_ADH_installer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='ACI_ADH_installer_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ACI_ADH_installer_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_16HR_Rigger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_16HR_Rigger_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_16HR_Rigger_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_30HR_CSM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_30HR_CSM_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_30HR_CSM_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Installer_Removal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Installer_Removal_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Installer_Removal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Riggers_Supervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Riggers_Supervisor_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Riggers_Supervisor_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Supp_Scaff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Supp_Scaff_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Supp_Scaff_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Suspended_Scaffold_Supervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Suspended_Scaffold_Supervisor_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_32HR_Suspended_Scaffold_Supervisor_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_Flagger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_Flagger_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_Flagger_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_supp_Scaff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_supp_Scaff_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_4HR_supp_Scaff_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Confind_Space',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Confind_Space_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Confind_Space_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Signal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Signal_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='DOB_8HR_Signal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_a35',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_a35_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_a35_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_e_21',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_e_21_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_e_21_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_f60',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_f60_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_f60_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s92',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s92_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s92_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s93',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s93_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='FDNY_s93_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='First_Aid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='First_Aid_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='First_Aid_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Forklift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='Forklift_Lift_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Forklift_Lift_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Incident_1_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Incident_2_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Incident_3_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='NCCOO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='NCCOO_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='NCCOO_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_30',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_30_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_30_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_ghs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_ghs_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='OSHA_ghs_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Pump_operator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='Pump_operator_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Pump_operator_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Drug_and_alcoh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Drug_and_alcoh_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Drug_and_alcoh_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_General_Electives',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_General_Electives_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_General_Electives_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Pre_Task_Safety',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Pre_Task_Safety_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Pre_Task_Safety_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Site_Safety_Plan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Site_Safety_Plan_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Site_Safety_Plan_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Specilized_Elective',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Specilized_Elective_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Specilized_Elective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Tool_Box_Meeting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Tool_Box_Meeting_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_2HR_Tool_Box_Meeting_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_Fall_protection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_Fall_protection_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_Fall_protection_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_SSM_Refresher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_SSM_Refresher_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_8HR_SSM_Refresher_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_Suppervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_Suppervisor_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_Suppervisor_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='SST_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Scissor_Lift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='Scissor_Lift_No',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Scissor_Lift_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='TITAN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bull_Float',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='disability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='disability_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='disability_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fire_Watch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='flagger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='grinding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='hand_Set_Forms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='helicopter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='incident_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='incident_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='incident_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='incident_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='layout',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='level_Column_Deck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='patching',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='pipe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='plywood_Deck',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='rebar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='rigger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='stairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='stripping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='trovell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='two_x_Four',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='vertical_Netting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='vibrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_1_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_2_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_3_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='warning_notice_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='wc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='wc_No',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='wc_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Disability',
        ),
        migrations.DeleteModel(
            name='Incident',
        ),
        migrations.DeleteModel(
            name='Licenses',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.DeleteModel(
            name='status',
        ),
        migrations.DeleteModel(
            name='WarningNotices',
        ),
        migrations.DeleteModel(
            name='WorkersCompensation',
        ),
    ]