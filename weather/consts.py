WEATHER_API_BASE = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
WEATHER_API_FORECAST = "http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"

DEFAULT_CITY = "KUALA_LUMPUR"

CITIES_INFO = {
    "KUALA_LUMPUR":
        {
            "city": "Kuala Lumpur",
            "lat": "3.1478",
            "lng": "101.6953",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kuala Lumpur",
            "capital": "primary",
            "population": "8285000",
            "population_proper": "1768000"
        },
    "KLANG":
        {
            "city": "Klang",
            "lat": "3.0333",
            "lng": "101.4500",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Selangor",
            "capital": "",
            "population": "878000",
            "population_proper": "878000"
        },
    "IPOH":
        {
            "city": "Ipoh",
            "lat": "4.6000",
            "lng": "101.0700",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Perak",
            "capital": "admin",
            "population": "866772",
            "population_proper": "866772"
        },
    "BUTTERWORTH":
        {
            "city": "Butterworth",
            "lat": "5.3942",
            "lng": "100.3664",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Pulau Pinang",
            "capital": "",
            "population": "821652",
            "population_proper": "107591"

        },
    "GEORGE_TOWN":
        {
            "city": "George Town",
            "lat": "5.4145",
            "lng": "100.3292",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Pulau Pinang",
            "capital": "admin",
            "population": "708127",
            "population_proper": "708127"

        },

    "PETALING_JAYA":
        {
            "city": "Petaling Jaya",
            "lat": "3.1073",
            "lng": "101.6067",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Selangor",
            "capital": "",
            "population": "638516",
            "population_proper": "638516"

        },

    "KUANTAN":
        {
            "city": "Kuantan",
            "lat": "3.8167",
            "lng": "103.3333",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Pahang",
            "capital": "admin",
            "population": "607778",
            "population_proper": "607778"

        },

    "SHAH_ALAM":
        {
            "city": "Shah Alam",
            "lat": "3.0833",
            "lng": "101.5333",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Selangor",
            "capital": "admin",
            "population": "584340",
            "population_proper": "584340"

        },

    "JOHOR_BAHRU":
        {
            "city": "Johor Bahru",
            "lat": "1.4556",
            "lng": "103.7611",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Johor",
            "capital": "admin",
            "population": "497097",
            "population_proper": "497097"

        },

    "KOTA_BHARU":
        {
            "city": "Kota Bharu",
            "lat": "6.1333",
            "lng": "102.2500",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "admin",
            "population": "491237",
            "population_proper": "491237"

        },

    "MELAKA":
        {
            "city": "Melaka",
            "lat": "2.1889",
            "lng": "102.2511",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Melaka",
            "capital": "admin",
            "population": "455300",
            "population_proper": "455300"

        },

    "KOTA_KINABALU":
        {
            "city": "Kota Kinabalu",
            "lat": "5.9750",
            "lng": "116.0725",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Sabah",
            "capital": "admin",
            "population": "452058",
            "population_proper": "452058"

        },

    "SEREMBAN":
        {
            "city": "Seremban",
            "lat": "2.7297",
            "lng": "101.9381",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Negeri Sembilan",
            "capital": "admin",
            "population": "419536",
            "population_proper": "419536"

        },

    "SANDAKAN":
        {
            "city": "Sandakan",
            "lat": "5.8388",
            "lng": "118.1173",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Sabah",
            "capital": "",
            "population": "396290",
            "population_proper": "396290"

        },

    "SUNGAI_PETANI":
        {
            "city": "Sungai Petani",
            "lat": "5.6500",
            "lng": "100.4800",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kedah",
            "capital": "",
            "population": "358499",
            "population_proper": "228843"

        },

    "KUCHING":
        {
            "city": "Kuching",
            "lat": "1.5397",
            "lng": "110.3542",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Sarawak",
            "capital": "admin",
            "population": "325132",
            "population_proper": "325132"

        },

    "KUALA_TERENGGANU":
        {
            "city": "Kuala Terengganu",
            "lat": "5.3303",
            "lng": "103.1408",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Terengganu",
            "capital": "admin",
            "population": "255109",
            "population_proper": "255109"

        },

    "ALOR_SETAR":
        {
            "city": "Alor Setar",
            "lat": "6.1167",
            "lng": "100.3667",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kedah",
            "capital": "admin",
            "population": "217000",
            "population_proper": "217000"

        },

    "PUTRAJAYA":
        {
            "city": "Putrajaya",
            "lat": "2.9140",
            "lng": "101.7019",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Putrajaya",
            "capital": "admin",
            "population": "67964",
            "population_proper": "50000"

        },

    "KANGAR":
        {
            "city": "Kangar",
            "lat": "6.4414",
            "lng": "100.1986",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Perlis",
            "capital": "admin",
            "population": "48898",
            "population_proper": "48898"

        },

    "LABUAN":
        {
            "city": "Labuan",
            "lat": "5.2803",
            "lng": "115.2475",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Labuan",
            "capital": "admin",
            "population": "",
            "population_proper": ""

        },

    "PASIR_MAS":
        {
            "city": "Pasir Mas",
            "lat": "6.0493",
            "lng": "102.1399",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "minor",
            "population": "",
            "population_proper": ""

        },

    "TUMPAT":
        {
            "city": "Tumpat",
            "lat": "6.2000",
            "lng": "102.1667",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "minor",
            "population": "",
            "population_proper": ""

        },

    "KETEREH":
        {
            "city": "Ketereh",
            "lat": "5.9570",
            "lng": "102.2482",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "minor",
            "population": "",
            "population_proper": ""

        },

    "KAMPUNG_LEMAL":
        {
            "city": "Kampung Lemal",
            "lat": "6.0302",
            "lng": "102.1413",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "minor",
            "population": "",
            "population_proper": ""

        },

    "PULAI_CHONDONG":
        {
            "city": "Pulai Chondong",
            "lat": "5.8713",
            "lng": "102.2318",
            "country": "Malaysia",
            "iso2": "MY",
            "admin_name": "Kelantan",
            "capital": "minor",
            "population": "",
            "population_proper": ""

        }
}
