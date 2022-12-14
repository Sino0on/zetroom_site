# Generated by Django 4.0.6 on 2022-08-07 13:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=100)),
                ('username_tg', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('tg', models.CharField(max_length=100)),
                ('age', models.DateField(blank=True, null=True)),
                ('rank', models.IntegerField(default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('hour', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/courses/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('education', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '????????',
                'verbose_name_plural': '??????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '???????????? ????????',
                'verbose_name_plural': '???????????? ????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/meeting/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '??????????????????????',
                'verbose_name_plural': '??????????????????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('Course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.course')),
            ],
            options={
                'verbose_name': '????????????',
                'verbose_name_plural': '??????????????',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='ImageMet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/meeting')),
                ('meet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='ImageCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/courses/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('maxstudent', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '????????????',
                'verbose_name_plural': '????????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='CourseFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
            ],
            options={
                'verbose_name': '???????? ?? ??????????',
                'verbose_name_plural': '?????????? ?? ??????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
            ],
            options={
                'verbose_name': '???????????? ???? ???????? ?? ??????????',
                'verbose_name_plural': '???????????? ???? ???????? ?? ??????????',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('groupcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.group')),
            ],
            options={
                'verbose_name': '?????????????? ????????',
                'verbose_name_plural': '?????????????? ??????????',
                'ordering': ['-date'],
                'unique_together': {('account', 'groupcourse')},
            },
        ),
        migrations.CreateModel(
            name='ApplicationMet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.meeting')),
            ],
            options={
                'verbose_name': '???????????? ???? ??????????????????????',
                'verbose_name_plural': '???????????? ???? ??????????????????????',
                'ordering': ['-date'],
                'unique_together': {('account', 'meeting')},
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.course')),
            ],
            options={
                'verbose_name': '????????????',
                'verbose_name_plural': '????????????',
                'ordering': ['-date'],
                'unique_together': {('account', 'course')},
            },
        ),
    ]
