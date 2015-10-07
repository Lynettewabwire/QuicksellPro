# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(default=None)),
                ('phoneNo', models.CharField(default=0, max_length=20)),
                ('country', models.CharField(max_length=30, choices=[(b'', b'Select Country'), (b'AF', b'Afghanistan'), (b'AL', b'Albania'), (b'DZ', b'Algeria'), (b'AS', b'American Samoa'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AI', b'Anguilla'), (b'AQ', b'Antarctica'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AW', b'Aruba'), (b'AU', b'Australia'), (b'AT', b'Austria'), (b'AZ', b'Azerbaijan'), (b'BS', b'Bahamas'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BZ', b'Belize'), (b'BJ', b'Benin'), (b'BM', b'Bermuda'), (b'BT', b'Bhutan'), (b'BO', b'Bolivia'), (b'BA', b'Bosnia and Herzegovina'), (b'BW', b'Botswana'), (b'BV', b'Bouvet Island'), (b'BR', b'Brazil'), (b'BQ', b'British Antarctic Territory'), (b'IO', b'British Indian Ocean Territory'), (b'VG', b'British Virgin Islands'), (b'BN', b'Brunei'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'KH', b'Cambodia'), (b'CM', b'Cameroon'), (b'CA', b'Canada'), (b'CT', b'Canton and Enderbury Islands'), (b'CV', b'Cape Verde'), (b'KY', b'Cayman Islands'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'China'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos [Keeling] Islands'), (b'CO', b'Colombia'), (b'KM', b'Comoros'), (b'CG', b'Congo - Brazzaville'), (b'CD', b'Congo - Kinshasa'), (b'CK', b'Cook Islands'), (b'CR', b'Costa Rica'), (b'HR', b'Croatia'), (b'CU', b'Cuba'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'CI', b"Cote d'Ivoire"), (b'DK', b'Denmark'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'NQ', b'Dronning Maud Land'), (b'DD', b'East Germany'), (b'EC', b'Ecuador'), (b'EG', b'Egypt'), (b'SV', b'El Salvador'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'EE', b'Estonia'), (b'ET', b'Ethiopia'), (b'FK', b'Falkland Islands'), (b'FO', b'Faroe Islands'), (b'FJ', b'Fiji'), (b'FI', b'Finland'), (b'FR', b'France'), (b'GF', b'French Guiana'), (b'PF', b'French Polynesia'), (b'TF', b'French Southern Territories'), (b'FQ', b'French Southern and Antarctic Territories'), (b'GA', b'Gabon'), (b'GM', b'Gambia'), (b'GE', b'Georgia'), (b'DE', b'Germany'), (b'GH', b'Ghana'), (b'GI', b'Gibraltar'), (b'GR', b'Greece'), (b'GL', b'Greenland'), (b'GD', b'Grenada'), (b'GP', b'Guadeloupe'), (b'GU', b'Guam'), (b'GT', b'Guatemala'), (b'GG', b'Guernsey'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HM', b'Heard Island and McDonald Islands'), (b'HN', b'Honduras'), (b'HK', b'Hong Kong SAR China'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran'), (b'IQ', b'Iraq'), (b'IE', b'Ireland'), (b'IM', b'Isle of Man'), (b'IL', b'Israel'), (b'IT', b'Italy'), (b'JM', b'Jamaica'), (b'JP', b'Japan'), (b'JE', b'Jersey'), (b'JT', b'Johnston Island'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KE', b'Kenya'), (b'KI', b'Kiribati'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b'Laos'), (b'LV', b'Latvia'), (b'LB', b'Lebanon'), (b'LS', b'Lesotho'), (b'LR', b'Liberia'), (b'LY', b'Libya'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MO', b'Macau SAR China'), (b'MK', b'Macedonia'), (b'MG', b'Madagascar'), (b'MW', b'Malawi'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'ML', b'Mali'), (b'MT', b'Malta'), (b'MH', b'Marshall Islands'), (b'MQ', b'Martinique'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'YT', b'Mayotte'), (b'FX', b'Metropolitan France'), (b'MX', b'Mexico'), (b'FM', b'Micronesia'), (b'MI', b'Midway Islands'), (b'MD', b'Moldova'), (b'MC', b'Monaco'), (b'MN', b'Mongolia'), (b'ME', b'Montenegro'), (b'MS', b'Montserrat'), (b'MA', b'Morocco'), (b'MZ', b'Mozambique'), (b'MM', b'Myanmar [Burma]'), (b'NA', b'Namibia'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NL', b'Netherlands'), (b'AN', b'Netherlands Antilles'), (b'NT', b'Neutral Zone'), (b'NC', b'New Caledonia'), (b'NZ', b'New Zealand'), (b'NI', b'Nicaragua'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'NU', b'Niue'), (b'NF', b'Norfolk Island'), (b'KP', b'North Korea'), (b'VD', b'North Vietnam'), (b'MP', b'Northern Mariana Islands'), (b'NO', b'Norway'), (b'OM', b'Oman'), (b'PC', b'Pacific Islands Trust Territory'), (b'PK', b'Pakistan'), (b'PW', b'Palau'), (b'PS', b'Palestinian Territories'), (b'PA', b'Panama'), (b'PZ', b'Panama Canal Zone'), (b'PG', b'Papua New Guinea'), (b'PY', b'Paraguay'), (b'YD', b"People's Democratic Republic of Yemen"), (b'PE', b'Peru'), (b'PH', b'Philippines'), (b'PN', b'Pitcairn Islands'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'PR', b'Puerto Rico'), (b'QA', b'Qatar'), (b'RO', b'Romania'), (b'RU', b'Russia'), (b'RW', b'Rwanda'), (b'RE', b'Reunion'), (b'BL', b'Saint Barthelemy'), (b'SH', b'Saint Helena'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'MF', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'VC', b'Saint Vincent and the Grenadines'), (b'WS', b'Samoa'), (b'SM', b'San Marino'), (b'SA', b'Saudi Arabia'), (b'SN', b'Senegal'), (b'RS', b'Serbia'), (b'CS', b'Serbia and Montenegro'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SG', b'Singapore'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'SB', b'Solomon Islands'), (b'SO', b'Somalia'), (b'ZA', b'South Africa'), (b'GS', b'South Georgia and the South Sandwich Islands'), (b'KR', b'South Korea'), (b'ES', b'Spain'), (b'LK', b'Sri Lanka'), (b'SD', b'Sudan'), (b'SR', b'Suriname'), (b'SJ', b'Svalbard and Jan Mayen'), (b'SZ', b'Swaziland'), (b'SE', b'Sweden'), (b'CH', b'Switzerland'), (b'SY', b'Syria'), (b'ST', b'Sao Tome and Principe'), (b'TW', b'Taiwan'), (b'TJ', b'Tajikistan'), (b'TZ', b'Tanzania'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste'), (b'TG', b'Togo'), (b'TK', b'Tokelau'), (b'TO', b'Tonga'), (b'TT', b'Trinidad and Tobago'), (b'TN', b'Tunisia'), (b'TR', b'Turkey'), (b'TM', b'Turkmenistan'), (b'TC', b'Turks and Caicos Islands'), (b'TV', b'Tuvalu'), (b'UM', b'U.S. Minor Outlying Islands'), (b'PU', b'U.S. Miscellaneous Pacific Islands'), (b'VI', b'U.S. Virgin Islands'), (b'UG', b'Uganda'), (b'UA', b'Ukraine'), (b'SU', b'Union of Soviet Socialist Republics'), (b'AE', b'United Arab Emirates'), (b'GB', b'United Kingdom'), (b'US', b'United States'), (b'ZZ', b'Unknown or Invalid Region'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekistan'), (b'VU', b'Vanuatu'), (b'VA', b'Vatican City'), (b'VE', b'Venezuela'), (b'VN', b'Vietnam'), (b'WK', b'Wake Island'), (b'WF', b'Wallis and Futuna'), (b'EH', b'Western Sahara'), (b'YE', b'Yemen'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe'), (b'AX', b'Aland Islands')])),
                ('city', models.CharField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_item', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
