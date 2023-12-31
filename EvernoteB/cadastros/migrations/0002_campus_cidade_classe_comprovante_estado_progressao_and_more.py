# Generated by Django 4.2.4 on 2023-08-15 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=150, verbose_name='endereço')),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nivel', models.IntegerField(verbose_name='nível')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Comprovante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
                ('data_final', models.DateField(blank=True, help_text='Informar apenas se o comprovante for relativo a um período.', null=True)),
                ('arquivo', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='Progressao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('observacao', models.CharField(max_length=255, verbose_name='observação')),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('siape', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimentado_em', models.DateTimeField(auto_now_add=True)),
                ('detalhes', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Validacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validado_em', models.DateTimeField(auto_now_add=True)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('justificativa', models.TextField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=models.CharField(max_length=255, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='detalhes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='pontos',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='campo',
            name='descricao',
            field=models.CharField(max_length=150, verbose_name='descrição'),
        ),
        migrations.AddConstraint(
            model_name='atividade',
            constraint=models.UniqueConstraint(fields=('numero', 'campo'), name='unica_num_atividade_campo'),
        ),
        migrations.AddField(
            model_name='validacao',
            name='comprovante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.comprovante'),
        ),
        migrations.AddField(
            model_name='validacao',
            name='validado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='situacao',
            name='movimentado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='situacao',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.status'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.campus'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
        migrations.AddField(
            model_name='progressao',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.classe', verbose_name='classe pretendida'),
        ),
        migrations.AddField(
            model_name='progressao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comprovante',
            name='atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.atividade'),
        ),
        migrations.AddField(
            model_name='comprovante',
            name='progressao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.progressao', verbose_name='progressão'),
        ),
        migrations.AddField(
            model_name='comprovante',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.estado'),
        ),
    ]
