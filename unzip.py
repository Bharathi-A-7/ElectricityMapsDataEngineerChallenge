import os
from pathlib import Path
import zipfile
import pickle

zip_file_name = 'Electricity Maps Data Engineering Challenge-20220811T074625Z-001.zip'

dataset_path = str(os.path.join(Path.home(), "Downloads", zip_file_name))
target_directory = str(os.path.join(Path.home(), "Documents", "ElectricityMaps", "datasets"))
working_directory = str(os.path.join(Path.home(), "Documents", "ElectricityMaps"))
#print(target_directory)

#Unzip the folder in the Downloads directory and extract the files into a new directory called 'datasets'
with zipfile.ZipFile(dataset_path, "r") as zip:
        for zip_info in zip.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip.extract(zip_info, target_directory)

#Map Zone IDs to actual names of the zones
zoneShortName =  {
    "AD": {
      "zoneName": "Andorra"
    },
    "AE": {
      "zoneName": "United Arab Emirates"
    },
    "AF": {
      "zoneName": "Afghanistan"
    },
    "AG": {
      "zoneName": "Antigua and Barbuda"
    },
    "AI": {
      "zoneName": "Anguilla"
    },
    "AL": {
      "zoneName": "Albania"
    },
    "AM": {
      "zoneName": "Armenia"
    },
    "AO": {
      "zoneName": "Angola"
    },
    "AQ": {
      "zoneName": "Antarctica"
    },
    "AR": {
      "zoneName": "Argentina"
    },
    "AS": {
      "zoneName": "American Samoa"
    },
    "AT": {
      "zoneName": "Austria"
    },
    "AUS-NSW": {
      "countryName": "Australia",
      "zoneName": "New South Wales"
    },
    "AUS-NT": {
      "countryName": "Australia",
      "zoneName": "Northern Territory"
    },
    "AUS-QLD": {
      "countryName": "Australia",
      "zoneName": "Queensland"
    },
    "AUS-SA": {
      "countryName": "Australia",
      "zoneName": "South Australia"
    },
    "AUS-TAS": {
      "countryName": "Australia",
      "zoneName": "Tasmania"
    },
    "AUS-TAS-CBI": {
      "countryName": "Australia",
      "zoneName": "Cape Barren Island"
    },
    "AUS-TAS-KI": {
      "countryName": "Australia",
      "zoneName": "King Island"
    },
    "AUS-TAS-FI": {
      "countryName": "Australia",
      "zoneName": "Flinders Island"
    },
    "AUS-VIC": {
      "countryName": "Australia",
      "zoneName": "Victoria"
    },
    "AUS-WA": {
      "countryName": "Australia",
      "zoneName": "Western Australia"
    },
    "AUS-WA-RI": {
      "countryName": "Australia",
      "zoneName": "Rottnest Island"
    },
    "AW": {
      "zoneName": "Aruba"
    },
    "AX": {
      "zoneName": "Åland Islands"
    },
    "AZ": {
      "zoneName": "Azerbaijan"
    },
    "BA": {
      "zoneName": "Bosnia and Herzegovina"
    },
    "BB": {
      "zoneName": "Barbados"
    },
    "BD": {
      "zoneName": "Bangladesh"
    },
    "BE": {
      "zoneName": "Belgium"
    },
    "BF": {
      "zoneName": "Burkina Faso"
    },
    "BG": {
      "zoneName": "Bulgaria"
    },
    "BH": {
      "zoneName": "Bahrain"
    },
    "BI": {
      "zoneName": "Burundi"
    },
    "BJ": {
      "zoneName": "Benin"
    },
    "BM": {
      "zoneName": "Bermuda"
    },
    "BN": {
      "zoneName": "Brunei"
    },
    "BO": {
      "zoneName": "Bolivia"
    },
    "BQ": {
      "zoneName": "Bonaire, Sint Eustatius and Saba"
    },
    "BR-CS": {
      "countryName": "Brazil",
      "zoneName": "Central Brazil"
    },
    "BR-I": {
      "countryName": "Brazil",
      "zoneName": "Isolated Systems"
    },
    "BR-N": {
      "countryName": "Brazil",
      "zoneName": "North Brazil"
    },
    "BR-NE": {
      "countryName": "Brazil",
      "zoneName": "North-East Brazil"
    },
    "BR-S": {
      "countryName": "Brazil",
      "zoneName": "South Brazil"
    },
    "BS": {
      "zoneName": "Bahamas"
    },
    "BT": {
      "zoneName": "Bhutan"
    },
    "BV": {
      "zoneName": "Bouvet Island"
    },
    "BW": {
      "zoneName": "Botswana"
    },
    "BY": {
      "zoneName": "Belarus"
    },
    "BZ": {
      "zoneName": "Belize"
    },
    "CA-AB": {
      "countryName": "Canada",
      "zoneName": "Alberta"
    },
    "CA-BC": {
      "countryName": "Canada",
      "zoneName": "British Columbia"
    },
    "CA-MB": {
      "countryName": "Canada",
      "zoneName": "Manitoba"
    },
    "CA-NB": {
      "countryName": "Canada",
      "zoneName": "New Brunswick"
    },
    "CA-NL": {
      "countryName": "Canada",
      "zoneName": "Newfoundland and Labrador"
    },
    "CA-NL-LB": {
      "countryName": "Canada",
      "zoneName": "Labrador"
    },
    "CA-NL-NF": {
      "countryName": "Canada",
      "zoneName": "Newfoundland"
    },
    "CA-NS": {
      "countryName": "Canada",
      "zoneName": "Nova Scotia"
    },
    "CA-NT": {
      "countryName": "Canada",
      "zoneName": "Northwest Territories"
    },
    "CA-NU": {
      "countryName": "Canada",
      "zoneName": "Nunavut"
    },
    "CA-ON": {
      "countryName": "Canada",
      "zoneName": "Ontario"
    },
    "CA-PE": {
      "countryName": "Canada",
      "zoneName": "Prince Edward Island"
    },
    "CA-QC": {
      "countryName": "Canada",
      "zoneName": "Québec"
    },
    "CA-SK": {
      "countryName": "Canada",
      "zoneName": "Saskatchewan"
    },
    "CA-YT": {
      "countryName": "Canada",
      "zoneName": "Yukon"
    },
    "CC": {
      "zoneName": "Cocos Islands"
    },
    "CD": {
      "zoneName": "Democratic Republic of the Congo"
    },
    "CF": {
      "zoneName": "Central African Republic"
    },
    "CG": {
      "zoneName": "Congo"
    },
    "CH": {
      "zoneName": "Switzerland"
    },
    "CI": {
      "zoneName": "Ivory Coast"
    },
    "CK": {
      "zoneName": "Cook Islands"
    },
    "CL-CHP": {
      "countryName": "Chile",
      "zoneName": "Easter Island"
    },
    "CL-SEA": {
      "countryName": "Chile",
      "zoneName": "Sistema Eléctrico de Aysén"
    },
    "CL-SEM": {
      "countryName": "Chile",
      "zoneName": "Sistema Eléctrico de Magallanes"
    },
    "CL-SEN": {
      "countryName": "Chile",
      "zoneName": "Sistema Eléctrico Nacional"
    },
    "CM": {
      "zoneName": "Cameroon"
    },
    "CN": {
      "zoneName": "China"
    },
    "CO": {
      "zoneName": "Colombia"
    },
    "CR": {
      "zoneName": "Costa Rica"
    },
    "CU": {
      "zoneName": "Cuba"
    },
    "CV": {
      "zoneName": "Cabo Verde"
    },
    "CW": {
      "zoneName": "Curaçao"
    },
    "CX": {
      "zoneName": "Christmas Island"
    },
    "CY": {
      "zoneName": "Cyprus"
    },
    "CZ": {
      "zoneName": "Czechia"
    },
    "DE": {
      "zoneName": "Germany"
    },
    "DJ": {
      "zoneName": "Djibouti"
    },
    "DK": {
      "zoneName": "Denmark"
    },
    "DK-DK1": {
      "countryName": "Denmark",
      "zoneName": "West Denmark"
    },
    "DK-DK2": {
      "countryName": "Denmark",
      "zoneName": "East Denmark"
    },
    "DK-BHM": {
      "countryName": "Denmark",
      "zoneName": "Bornholm"
    },
    "DM": {
      "zoneName": "Dominica"
    },
    "DO": {
      "zoneName": "Dominican Republic"
    },
    "DZ": {
      "zoneName": "Algeria"
    },
    "EC": {
      "zoneName": "Ecuador"
    },
    "EE": {
      "zoneName": "Estonia"
    },
    "EG": {
      "zoneName": "Egypt"
    },
    "EH": {
      "zoneName": "Western Sahara"
    },
    "ER": {
      "zoneName": "Eritrea"
    },
    "ES": {
      "zoneName": "Spain"
    },
    "ES-CE": {
      "countryName": "Spain",
      "zoneName": "Ceuta"
    },
    "ES-IB-FO": {
      "countryName": "Spain",
      "zoneName": "Formentera"
    },
    "ES-IB-IZ": {
      "countryName": "Spain",
      "zoneName": "Ibiza"
    },
    "ES-IB-MA": {
      "countryName": "Spain",
      "zoneName": "Mallorca"
    },
    "ES-IB-ME": {
      "countryName": "Spain",
      "zoneName": "Menorca"
    },
    "ES-CN-FVLZ": {
      "countryName": "Spain",
      "zoneName": "Fuerteventura/Lanzarote"
    },
    "ES-CN-GC": {
      "countryName": "Spain",
      "zoneName": "Gran Canaria"
    },
    "ES-CN-HI": {
      "countryName": "Spain",
      "zoneName": "El Hierro"
    },
    "ES-CN-IG": {
      "countryName": "Spain",
      "zoneName": "Isla de la Gomera"
    },
    "ES-CN-LP": {
      "countryName": "Spain",
      "zoneName": "La Palma"
    },
    "ES-CN-TE": {
      "countryName": "Spain",
      "zoneName": "Tenerife"
    },
    "ES-ML": {
      "countryName": "Spain",
      "zoneName": "Melilla"
    },
    "ET": {
      "zoneName": "Ethiopia"
    },
    "FI": {
      "zoneName": "Finland"
    },
    "FJ": {
      "zoneName": "Fiji"
    },
    "FK": {
      "zoneName": "Falkland Islands"
    },
    "FM": {
      "zoneName": "Micronesia"
    },
    "FO": {
      "zoneName": "Faroe Islands"
    },
    "FO-MI": {
      "countryName": "Faroe Islands",
      "zoneName": "Main Islands"
    },
    "FO-SI": {
      "countryName": "Faroe Islands",
      "zoneName": "South Island"
    },
    "FR": {
      "zoneName": "France"
    },
    "FR-COR": {
      "countryName": "France",
      "zoneName": "Corsica"
    },
    "GA": {
      "zoneName": "Gabon"
    },
    "GB": {
      "zoneName": "Great Britain"
    },
    "GB-NIR": {
      "zoneName": "Northern Ireland"
    },
    "GB-ORK": {
      "countryName": "Great Britain",
      "zoneName": "Orkney Islands"
    },
    "GB-SHI": {
      "countryName": "Great Britain",
      "zoneName": "Shetland Islands"
    },
    "GB-ZET": {
      "countryName": "Great Britain",
      "zoneName": "Shetland Islands"
    },
    "GD": {
      "zoneName": "Grenada"
    },
    "GE": {
      "zoneName": "Georgia"
    },
    "GF": {
      "zoneName": "French Guiana"
    },
    "GG": {
      "zoneName": "Guernsey"
    },
    "GH": {
      "zoneName": "Ghana"
    },
    "GI": {
      "zoneName": "Gibraltar"
    },
    "GL": {
      "zoneName": "Greenland"
    },
    "GM": {
      "zoneName": "Gambia"
    },
    "GN": {
      "zoneName": "Guinea"
    },
    "GP": {
      "zoneName": "Guadeloupe"
    },
    "GQ": {
      "zoneName": "Equatorial Guinea"
    },
    "GR": {
      "zoneName": "Greece"
    },
    "GR-IS": {
      "countryName": "Greece",
      "zoneName": "Aegean Islands"
    },
    "GS": {
      "zoneName": "South Georgia and the South Sandwich Islands"
    },
    "GT": {
      "zoneName": "Guatemala"
    },
    "GU": {
      "zoneName": "Guam"
    },
    "GW": {
      "zoneName": "Guinea-Bissau"
    },
    "GY": {
      "zoneName": "Guyana"
    },
    "HK": {
      "zoneName": "Hong Kong"
    },
    "HM": {
      "zoneName": "Heard Island and McDonald Islands"
    },
    "HN": {
      "zoneName": "Honduras"
    },
    "HR": {
      "zoneName": "Croatia"
    },
    "HT": {
      "zoneName": "Haiti"
    },
    "HU": {
      "zoneName": "Hungary"
    },
    "ID": {
      "zoneName": "Indonesia"
    },
    "IE": {
      "zoneName": "Ireland"
    },
    "IL": {
      "zoneName": "Israel"
    },
    "IM": {
      "zoneName": "Isle of Man"
    },
    "IN-AN": {
      "countryName": "India",
      "zoneName": "Andaman and Nicobar Islands"
    },
    "IN-AP": {
      "countryName": "India",
      "zoneName": "Andhra Pradesh"
    },
    "IN-AR": {
      "countryName": "India",
      "zoneName": "Arunachal Pradesh"
    },
    "IN-AS": {
      "countryName": "India",
      "zoneName": "Assam"
    },
    "IN-BR": {
      "countryName": "India",
      "zoneName": "Bihar"
    },
    "IN-CT": {
      "countryName": "India",
      "zoneName": "Chhattisgarh"
    },
    "IN-DL": {
      "countryName": "India",
      "zoneName": "Delhi"
    },
    "IN-DN": {
      "countryName": "India",
      "zoneName": "Dadra and Nagar Haveli"
    },
    "IN-GA": {
      "countryName": "India",
      "zoneName": "Goa"
    },
    "IN-GJ": {
      "countryName": "India",
      "zoneName": "Gujarat"
    },
    "IN-HP": {
      "countryName": "India",
      "zoneName": "Himachal Pradesh"
    },
    "IN-HR": {
      "countryName": "India",
      "zoneName": "Haryana"
    },
    "IN-JH": {
      "countryName": "India",
      "zoneName": "Jharkhand"
    },
    "IN-JK": {
      "countryName": "India",
      "zoneName": "Jammu and Kashmir"
    },
    "IN-KA": {
      "countryName": "India",
      "zoneName": "Karnataka"
    },
    "IN-KL": {
      "countryName": "India",
      "zoneName": "Kerala"
    },
    "IN-MH": {
      "countryName": "India",
      "zoneName": "Maharashtra"
    },
    "IN-ML": {
      "countryName": "India",
      "zoneName": "Meghalaya"
    },
    "IN-MN": {
      "countryName": "India",
      "zoneName": "Manipur"
    },
    "IN-MP": {
      "countryName": "India",
      "zoneName": "Madhya Pradesh"
    },
    "IN-MZ": {
      "countryName": "India",
      "zoneName": "Mizoram"
    },
    "IN-NL": {
      "countryName": "India",
      "zoneName": "Nagaland"
    },
    "IN-OR": {
      "countryName": "India",
      "zoneName": "Orissa"
    },
    "IN-PB": {
      "countryName": "India",
      "zoneName": "Punjab"
    },
    "IN-PY": {
      "countryName": "India",
      "zoneName": "Pondicherry"
    },
    "IN-RJ": {
      "countryName": "India",
      "zoneName": "Rajasthan"
    },
    "IN-SK": {
      "countryName": "India",
      "zoneName": "Sikkim"
    },
    "IN-TN": {
      "countryName": "India",
      "zoneName": "Tamil Nadu"
    },
    "IN-TR": {
      "countryName": "India",
      "zoneName": "Tripura"
    },
    "IN-UP": {
      "countryName": "India",
      "zoneName": "Uttar Pradesh"
    },
    "IN-UT": {
      "countryName": "India",
      "zoneName": "Uttarakhand"
    },
    "IN-WB": {
      "countryName": "India",
      "zoneName": "West Bengal"
    },
    "IO": {
      "zoneName": "British Indian Ocean Territory"
    },
    "IQ": {
      "zoneName": "Iraq"
    },
    "IQ-KUR": {
      "countryName": "Iraq",
      "zoneName": "Kurdistan"
    },
    "IR": {
      "zoneName": "Iran"
    },
    "IS": {
      "zoneName": "Iceland"
    },
    "IT": {
      "zoneName": "Italy"
    },
    "IT-CNO": {
      "countryName": "Italy",
      "zoneName": "Central North"
    },
    "IT-CSO": {
      "countryName": "Italy",
      "zoneName": "Central South"
    },
    "IT-NO": {
      "countryName": "Italy",
      "zoneName": "North"
    },
    "IT-SAR": {
      "countryName": "Italy",
      "zoneName": "Sardinia"
    },
    "IT-SIC": {
      "countryName": "Italy",
      "zoneName": "Sicily"
    },
    "IT-SO": {
      "countryName": "Italy",
      "zoneName": "South"
    },
    "JE": {
      "zoneName": "Jersey"
    },
    "JM": {
      "zoneName": "Jamaica"
    },
    "JO": {
      "zoneName": "Jordan"
    },
    "JP-CB": {
      "countryName": "Japan",
      "zoneName": "Chūbu"
    },
    "JP-CG": {
      "countryName": "Japan",
      "zoneName": "Chūgoku"
    },
    "JP-HKD": {
      "countryName": "Japan",
      "zoneName": "Hokkaidō"
    },
    "JP-HR": {
      "countryName": "Japan",
      "zoneName": "Hokuriku"
    },
    "JP-KN": {
      "countryName": "Japan",
      "zoneName": "Kansai"
    },
    "JP-KY": {
      "countryName": "Japan",
      "zoneName": "Kyūshū"
    },
    "JP-ON": {
      "countryName": "Japan",
      "zoneName": "Okinawa"
    },
    "JP-SK": {
      "countryName": "Japan",
      "zoneName": "Shikoku"
    },
    "JP-TH": {
      "countryName": "Japan",
      "zoneName": "Tōhoku"
    },
    "JP-TK": {
      "countryName": "Japan",
      "zoneName": "Tōkyō"
    },
    "KE": {
      "zoneName": "Kenya"
    },
    "KG": {
      "zoneName": "Kyrgyzstan"
    },
    "KH": {
      "zoneName": "Cambodia"
    },
    "KI": {
      "zoneName": "Kiribati"
    },
    "KM": {
      "zoneName": "Comoros"
    },
    "KN": {
      "zoneName": "Saint Kitts and Nevis"
    },
    "KP": {
      "zoneName": "North Korea"
    },
    "KR": {
      "zoneName": "South Korea"
    },
    "KW": {
      "zoneName": "Kuwait"
    },
    "KY": {
      "zoneName": "Cayman Islands"
    },
    "KZ": {
      "zoneName": "Kazakhstan"
    },
    "LA": {
      "zoneName": "Laos"
    },
    "LB": {
      "zoneName": "Lebanon"
    },
    "LC": {
      "zoneName": "Saint Lucia"
    },
    "LI": {
      "zoneName": "Liechtenstein"
    },
    "LK": {
      "zoneName": "Sri Lanka"
    },
    "LR": {
      "zoneName": "Liberia"
    },
    "LS": {
      "zoneName": "Lesotho"
    },
    "LT": {
      "zoneName": "Lithuania"
    },
    "LU": {
      "zoneName": "Luxembourg"
    },
    "LV": {
      "zoneName": "Latvia"
    },
    "LY": {
      "zoneName": "Libya"
    },
    "MA": {
      "zoneName": "Morocco"
    },
    "MC": {
      "zoneName": "Monaco"
    },
    "MD": {
      "zoneName": "Moldova"
    },
    "ME": {
      "zoneName": "Montenegro"
    },
    "MF": {
      "countryName": "Saint Martin",
      "zoneName": "French"
    },
    "MG": {
      "zoneName": "Madagascar"
    },
    "MH": {
      "zoneName": "Marshall Islands"
    },
    "MK": {
      "zoneName": "North Macedonia"
    },
    "ML": {
      "zoneName": "Mali"
    },
    "MM": {
      "zoneName": "Myanmar"
    },
    "MN": {
      "zoneName": "Mongolia"
    },
    "MO": {
      "zoneName": "Macao"
    },
    "MP": {
      "zoneName": "Northern Mariana Islands"
    },
    "MQ": {
      "zoneName": "Martinique"
    },
    "MR": {
      "zoneName": "Mauritania"
    },
    "MS": {
      "zoneName": "Montserrat"
    },
    "MT": {
      "zoneName": "Malta"
    },
    "MU": {
      "zoneName": "Mauritius"
    },
    "MV": {
      "zoneName": "Maldives"
    },
    "MW": {
      "zoneName": "Malawi"
    },
    "MX": {
      "zoneName": "Mexico"
    },
    "MX-BC": {
      "countryName": "Mexico",
      "zoneName": "Baja California"
    },
    "MX-CE": {
      "countryName": "Mexico",
      "zoneName": "Central"
    },
    "MX-NE": {
      "countryName": "Mexico",
      "zoneName": "North East"
    },
    "MX-NO": {
      "countryName": "Mexico",
      "zoneName": "North"
    },
    "MX-NW": {
      "countryName": "Mexico",
      "zoneName": "North West"
    },
    "MX-OC": {
      "countryName": "Mexico",
      "zoneName": "Occidental"
    },
    "MX-OR": {
      "countryName": "Mexico",
      "zoneName": "Oriental"
    },
    "MX-PN": {
      "countryName": "Mexico",
      "zoneName": "Peninsula"
    },
    "MY-EM": {
      "countryName": "Malaysia",
      "zoneName": "Borneo"
    },
    "MY-WM": {
      "countryName": "Malaysia",
      "zoneName": "Peninsula"
    },
    "MZ": {
      "zoneName": "Mozambique"
    },
    "NA": {
      "zoneName": "Namibia"
    },
    "NC": {
      "zoneName": "New Caledonia"
    },
    "NE": {
      "zoneName": "Niger"
    },
    "NF": {
      "zoneName": "Norfolk Island"
    },
    "NG": {
      "zoneName": "Nigeria"
    },
    "NI": {
      "zoneName": "Nicaragua"
    },
    "NKR": {
      "zoneName": "Nagorno-Karabakh"
    },
    "NL": {
      "zoneName": "Netherlands"
    },
    "NO-NO1": {
      "countryName": "Norway",
      "zoneName": "Southeast Norway"
    },
    "NO-NO2": {
      "countryName": "Norway",
      "zoneName": "Southwest Norway"
    },
    "NO-NO3": {
      "countryName": "Norway",
      "zoneName": "Middle Norway"
    },
    "NO-NO4": {
      "countryName": "Norway",
      "zoneName": "North Norway"
    },
    "NO-NO5": {
      "countryName": "Norway",
      "zoneName": "West Norway"
    },
    "NP": {
      "zoneName": "Nepal"
    },
    "NR": {
      "zoneName": "Nauru"
    },
    "NU": {
      "zoneName": "Niue"
    },
    "NZ": {
      "zoneName": "New Zealand"
    },
    "NZ-NZA": {
      "countryName": "New Zealand",
      "zoneName": "Auckland Islands"
    },
    "NZ-NZC": {
      "countryName": "New Zealand",
      "zoneName": "Chatham Islands"
    },
    "NZ-NZST": {
      "countryName": "New Zealand",
      "zoneName": "Stewart Island"
    },
    "OM": {
      "zoneName": "Oman"
    },
    "PA": {
      "zoneName": "Panama"
    },
    "PE": {
      "zoneName": "Peru"
    },
    "PF": {
      "zoneName": "French Polynesia"
    },
    "PG": {
      "zoneName": "Papua New Guinea"
    },
    "PH": {
      "zoneName": "Philippines"
    },
    "PK": {
      "zoneName": "Pakistan"
    },
    "PL": {
      "zoneName": "Poland"
    },
    "PM": {
      "zoneName": "Saint Pierre and Miquelon"
    },
    "PN": {
      "zoneName": "Pitcairn"
    },
    "PR": {
      "zoneName": "Puerto Rico"
    },
    "PS": {
      "zoneName": "State of Palestine"
    },
    "PT": {
      "zoneName": "Portugal"
    },
    "PT-AC": {
      "countryName": "Portugal",
      "zoneName": "Azores"
    },
    "PT-MA": {
      "countryName": "Portugal",
      "zoneName": "Madeira"
    },
    "PW": {
      "zoneName": "Palau"
    },
    "PY": {
      "zoneName": "Paraguay"
    },
    "QA": {
      "zoneName": "Qatar"
    },
    "RE": {
      "zoneName": "Réunion"
    },
    "RO": {
      "zoneName": "Romania"
    },
    "RS": {
      "zoneName": "Serbia"
    },
    "RU": {
      "zoneName": "Russia"
    },
    "RU-1": {
      "countryName": "Russia",
      "zoneName": "Europe-Ural"
    },
    "RU-2": {
      "countryName": "Russia",
      "zoneName": "Siberia"
    },
    "RU-AS": {
      "countryName": "Russia",
      "zoneName": "East"
    },
    "RU-EU": {
      "countryName": "Russia",
      "zoneName": "Arctic"
    },
    "RU-FE": {
      "countryName": "Russia",
      "zoneName": "Far East"
    },
    "RU-KGD": {
      "countryName": "Russia",
      "zoneName": "Kaliningrad"
    },
    "RW": {
      "zoneName": "Rwanda"
    },
    "SA": {
      "zoneName": "Saudi Arabia"
    },
    "SB": {
       "zoneName": "Solomon Islands"
    },
    "SC": {
      "zoneName": "Seychelles"
    },
    "SD": {
      "zoneName": "Sudan"
    },
    "SE": {
      "zoneName": "Sweden"
    },
    "SG": {
      "zoneName": "Singapore"
    },
    "SH": {
      "zoneName": "Saint Helena, Ascension and Tristan da Cunha"
    },
    "SI": {
      "zoneName": "Slovenia"
    },
    "SJ": {
      "zoneName": "Svalbard and Jan Mayen"
    },
    "SK": {
      "zoneName": "Slovakia"
    },
    "SL": {
      "zoneName": "Sierra Leone"
    },
    "SM": {
      "zoneName": "San Marino"
    },
    "SN": {
      "zoneName": "Senegal"
    },
    "SO": {
      "zoneName": "Somalia"
    },
    "SR": {
      "zoneName": "Suriname"
    },
    "SS": {
      "zoneName": "South Sudan"
    },
    "ST": {
      "zoneName": "Sao Tome and Principe"
    },
    "SV": {
      "zoneName": "El Salvador"
    },
    "SX": {
      "countryName": "Sint Maarten",
      "zoneName": "Dutch"
    },
    "SY": {
      "zoneName": "Syria"
    },
    "SZ": {
      "zoneName": "Swaziland"
    },
    "TC": {
      "zoneName": "Turks and Caicos Islands"
    },
    "TD": {
      "zoneName": "Chad"
    },
    "TF": {
      "zoneName": "French Southern Territories"
    },
    "TG": {
      "zoneName": "Togo"
    },
    "TH": {
      "zoneName": "Thailand"
    },
    "TJ": {
      "zoneName": "Tajikistan"
    },
    "TK": {
      "zoneName": "Tokelau"
    },
    "TL": {
      "zoneName": "Timor-Leste"
    },
    "TM": {
      "zoneName": "Turkmenistan"
    },
    "TN": {
      "zoneName": "Tunisia"
    },
    "TO": {
      "zoneName": "Tonga"
    },
    "TR": {
      "zoneName": "Turkey"
    },
    "TT": {
      "zoneName": "Trinidad and Tobago"
    },
    "TV": {
      "zoneName": "Tuvalu"
    },
    "TW": {
      "zoneName": "Taiwan"
    },
    "TZ": {
      "zoneName": "Tanzania"
    },
    "UA": {
      "zoneName": "Ukraine"
    },
    "UA-CR": {
      "countryName": "Ukraine",
      "zoneName": "Crimea"
    },
    "UG": {
      "zoneName": "Uganda"
    },
    "UM": {
      "zoneName": "United States Minor Outlying Islands"
    },
    "US-HI-HA": {
      "countryName": "USA",
      "zoneName": "Hawaii"
    },
    "US-HI-KA": {
      "countryName": "USA",
      "zoneName": "Kauai"
    },
    "US-HI-KH": {
      "countryName": "USA",
      "zoneName": "Kahoolawe"
    },
    "US-HI-LA": {
      "countryName": "USA",
      "zoneName": "Lanai"
    },
    "US-HI-MA": {
      "countryName": "USA",
      "zoneName": "Maui"
    },
    "US-HI-MO": {
      "countryName": "USA",
      "zoneName": "Molokai"
    },
    "US-HI-NI": {
      "countryName": "USA",
      "zoneName": "Niihau"
    },
    "US-HI-OA": {
      "countryName": "USA",
      "zoneName": "Oahu"
    },
    "US-CAL-BANC": {
      "countryName": "USA",
      "zoneName": "Balancing Authority Of Northern California"
    },
    "US-CAL-CISO": {
      "countryName": "USA",
      "zoneName": "California Independent System Operator"
    },
    "US-CAL-IID": {
      "countryName": "USA",
      "zoneName": "Imperial Irrigation District"
    },
    "US-CAL-LDWP": {
      "countryName": "USA",
      "zoneName": "Los Angeles Department Of Water And Power"
    },
    "US-CAL-TIDC": {
      "countryName": "USA",
      "zoneName": "Turlock Irrigation District"
    },
    "US-CAR-CPLE": {
      "countryName": "USA",
      "zoneName": "Duke Energy Progress East"
    },
    "US-CAR-CPLW": {
      "countryName": "USA",
      "zoneName": "Duke Energy Progress West"
    },
    "US-CAR-DUK": {
      "countryName": "USA",
      "zoneName": "Duke Energy Carolinas"
    },
    "US-CAR-SC": {
      "countryName": "USA",
      "zoneName": "South Carolina Public Service Authority"
    },
    "US-CAR-SCEG": {
      "countryName": "USA",
      "zoneName": "South Carolina Electric & Gas Company"
    },
    "US-CAR-YAD": {
      "countryName": "USA",
      "zoneName": "Alcoa Power Generating, Inc. Yadkin Division"
    },
    "US-CENT-SPA": {
      "countryName": "USA",
      "zoneName": "Southwestern Power Administration"
    },
    "US-CENT-SWPP": {
      "countryName": "USA",
      "zoneName": "Southwest Power Pool"
    },
    "US-FLA-FMPP": {
      "countryName": "USA",
      "zoneName": "Florida Municipal Power Pool"
    },
    "US-FLA-FPC": {
      "countryName": "USA",
      "zoneName": "Duke Energy Florida Inc"
    },
    "US-FLA-FPL": {
      "countryName": "USA",
      "zoneName": "Florida Power & Light Company"
    },
    "US-FLA-GVL": {
      "countryName": "USA",
      "zoneName": "Gainesville Regional Utilities"
    },
    "US-FLA-HST": {
      "countryName": "USA",
      "zoneName": "City Of Homestead"
    },
    "US-FLA-JEA": {
      "countryName": "USA",
      "zoneName": "Jacksonville Electric Authority"
    },
    "US-FLA-NSB": {
      "countryName": "USA",
      "zoneName": "Utilities Commission Of New Smyrna Beach"
    },
    "US-FLA-SEC": {
      "countryName": "USA",
      "zoneName": "Seminole Electric Cooperative"
    },
    "US-FLA-TAL": {
      "countryName": "USA",
      "zoneName": "City Of Tallahassee"
    },
    "US-FLA-TEC": {
      "countryName": "USA",
      "zoneName": "Tampa Electric Company"
    },
    "US-MIDA-PJM": {
      "countryName": "USA",
      "zoneName": "PJM Interconnection, Llc"
    },
    "US-MIDW-AECI": {
      "countryName": "USA",
      "zoneName": "Associated Electric Cooperative, Inc."
    },
    "US-MIDW-GLHB": {
      "countryName": "USA",
      "zoneName": "GridLiance"
    },
    "US-MIDW-LGEE": {
      "countryName": "USA",
      "zoneName": "Louisville Gas And Electric Company And Kentucky Utilities"
    },
    "US-MIDW-MISO": {
      "countryName": "USA",
      "zoneName": "Midcontinent Independent Transmission System Operator, Inc."
    },
    "US-NE-ISNE": {
      "countryName": "USA",
      "zoneName": "Iso New England Inc."
    },
    "US-NW-AVA": {
      "countryName": "USA",
      "zoneName": "Avista Corporation"
    },
    "US-NW-AVRN": {
      "countryName": "USA",
      "zoneName": "Avangrid Renewables Cooperative"
    },
    "US-NW-BPAT": {
      "countryName": "USA",
      "zoneName": "Bonneville Power Administration"
    },
    "US-NW-CHPD": {
      "countryName": "USA",
      "zoneName": "PUD No. 1 Of Chelan County"
    },
    "US-NW-DOPD": {
      "countryName": "USA",
      "zoneName": "PUD No. 1 Of Douglas County"
    },
    "US-NW-GCPD": {
      "countryName": "USA",
      "zoneName": "PUD No. 2 Of Grant County, Washington"
    },
    "US-NW-GRID": {
      "countryName": "USA",
      "zoneName": "Gridforce Energy Management, Llc"
    },
    "US-NW-GWA": {
      "countryName": "USA",
      "zoneName": "Naturener Power Watch, Llc (Gwa)"
    },
    "US-NW-IPCO": {
      "countryName": "USA",
      "zoneName": "Idaho Power Company"
    },
    "US-NW-NEVP": {
      "countryName": "USA",
      "zoneName": "Nevada Power Company"
    },
    "US-NW-NWMT": {
      "countryName": "USA",
      "zoneName": "Northwestern Energy"
    },
    "US-NW-PACE": {
      "countryName": "USA",
      "zoneName": "Pacificorp East"
    },
    "US-NW-PACW": {
      "countryName": "USA",
      "zoneName": "Pacificorp West"
    },
    "US-NW-PGE": {
      "countryName": "USA",
      "zoneName": "Portland General Electric Company"
    },
    "US-NW-PSCO": {
      "countryName": "USA",
      "zoneName": "Public Service Company Of Colorado"
    },
    "US-NW-PSEI": {
      "countryName": "USA",
      "zoneName": "Puget Sound Energy"
    },
    "US-NW-SCL": {
      "countryName": "USA",
      "zoneName": "Seattle City Light"
    },
    "US-NW-TPWR": {
      "countryName": "USA",
      "zoneName": "City Of Tacoma, Department Of Public Utilities, Light Division"
    },
    "US-NW-WACM": {
      "countryName": "USA",
      "zoneName": "Western Area Power Administration - Rocky Mountain Region"
    },
    "US-NW-WAUW": {
      "countryName": "USA",
      "zoneName": "Western Area Power Administration UGP West"
    },
    "US-NW-WWA": {
      "countryName": "USA",
      "zoneName": "Naturener Wind Watch, Llc"
    },
    "US-NY-NYIS": {
      "countryName": "USA",
      "zoneName": "New York Independent System Operator"
    },
    "US-SE-AEC": {
      "countryName": "USA",
      "zoneName": "Powersouth Energy Cooperative"
    },
    "US-SE-SEPA": {
      "countryName": "USA",
      "zoneName": "Southeastern Power Administration"
    },
    "US-SE-SOCO": {
      "countryName": "USA",
      "zoneName": "Southern Company Services, Inc. - Trans"
    },
    "US-SW-AZPS": {
      "countryName": "USA",
      "zoneName": "Arizona Public Service Company"
    },
    "US-SW-DEAA": {
      "countryName": "USA",
      "zoneName": "Arlington Valley, LLC"
    },
    "US-SW-EPE": {
      "countryName": "USA",
      "zoneName": "El Paso Electric Company"
    },
    "US-SW-GRIF": {
      "countryName": "USA",
      "zoneName": "Griffith Energy, LLC"
    },
    "US-SW-GRMA": {
      "countryName": "USA",
      "zoneName": "Gila River Power, LLC"
    },
    "US-SW-HGMA": {
      "countryName": "USA",
      "zoneName": "New Harquahala Generating Company, LLC"
    },
    "US-SW-PNM": {
      "countryName": "USA",
      "zoneName": "Public Service Company Of New Mexico"
    },
    "US-SW-SRP": {
      "countryName": "USA",
      "zoneName": "Salt River Project"
    },
    "US-SW-TEPC": {
      "countryName": "USA",
      "zoneName": "Tucson Electric Power Company"
    },
    "US-SW-WALC": {
      "countryName": "USA",
      "zoneName": "Western Area Power Administration - Desert Southwest Region"
    },
    "US-TEN-TVA": {
      "countryName": "USA",
      "zoneName": "Tennessee Valley Authority"
    },
    "US-TEX-ERCO": {
      "countryName": "USA",
      "zoneName": "Electric Reliability Council Of Texas, Inc."
    },
    "UY": {
      "zoneName": "Uruguay"
    },
    "UZ": {
      "zoneName": "Uzbekistan"
    },
    "VA": {
      "zoneName": "Vatican City"
    },
    "VC": {
      "zoneName": "Saint Vincent and the Grenadines"
    },
    "VE": {
      "zoneName": "Venezuela"
    },
    "VG": {
      "countryName": "Virgin Islands",
      "zoneName": "Virgin Islands"
    },
    "VI": {
      "countryName": "USA",
      "zoneName": "Virgin Islands"
    },
    "VN": {
      "zoneName": "Vietnam"
    },
    "VU": {
      "zoneName": "Vanuatu"
    },
    "WF": {
      "zoneName": "Wallis and Futuna"
    },
    "WS": {
      "zoneName": "Samoa"
    },
    "XK": {
      "zoneName": "Kosovo"
    },
    "XX": {
      "zoneName": "Northern Cyprus"
    },
    "YE": {
      "zoneName": "Yemen"
    },
    "YT": {
      "zoneName": "Mayotte"
    },
    "ZA": {
      "zoneName": "South Africa"
    },
    "ZM": {
      "zoneName": "Zambia"
    },
    "ZW": {
      "zoneName": "Zimbabwe"
    }
  }

zoneid_mapping = {key: value['zoneName'] for key, value in zoneShortName.items()}

with open(working_directory + '/zone_mapping.pickle', 'wb') as f:
    pickle.dump(zoneid_mapping, f, protocol=pickle.HIGHEST_PROTOCOL)


