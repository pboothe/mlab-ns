# Name of the entry in the Nagios table, containing the default
# configuration.
DEFAULT_NAGIOS_ENTRY = 'default'

# Earth radius in km.
EARTH_RADIUS = 6371

# Geolocation type values.
GEOLOCATION_APP_ENGINE = 'app_engine'
GEOLOCATION_MAXMIND = 'maxmind'
GEOLOCATION_USER_DEFINED = 'user_defined'

# Maximum number of entities fetched from datastore in a single query.
MAX_FETCHED_RESULTS = 500

# Service state status values from Nagios:
# OK            0
# WARNING       1
# CRITICAL      2
# UNKNOWN       3
NAGIOS_SERVICE_STATUS_OK = '0'

# Maximum number of entities fetched from datastore in a single query.
GQL_BATCH_SIZE = 1000

# Name of the encryption key used by the RegistrationClient.
REGISTRATION_KEY_ID = 'admin'

# Country code representing an unknown country location. This is automatically
# added in the X-AppEngine-Country header if AppEngine cannot determine the
# location.
UNKNOWN_COUNTRY = 'ZZ'
UNKNOWN_CITY = 'Zion'



