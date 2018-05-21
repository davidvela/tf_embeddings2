"&---------------------------------------------------------------------"
"& Report  ZMMM2
"&        rest ws call elastic
"&---------------------------------------------------------------------"
"&   22.05.2018 -  David Vela - Creation
"&---------------------------------------------------------------------"
class ELASTIC IMPLEMENTATION.
  METHOD constructor.
      cl_abap_string_utilities=>c2str_preserving_blanks(
        exporting source = ': '
        importing dest   = c_colon ) .
      cl_abap_string_utilities=>c2str_preserving_blanks(
        exporting source = ', '
        importing dest   = c_comma ) .

      CALL METHOD cl_http_client=>create
        EXPORTING
          host               = host
          service            = service
          proxy_host         = proxy_host
          proxy_service      = proxy_service
        IMPORTING
          client             = elastic_client
        EXCEPTIONS
          argument_not_found = 1
          internal_error     = 2
          plugin_not_active  = 3
          OTHERS             = 4.

      CALL METHOD elastic_client->authenticate
        EXPORTING
          username = 'user'
          password = 'password!'.

      IF https IS INITIAL.
        CONCATENATE 'http://' host ':' service '/' index '/' type '/' INTO url_base.
      ELSE.
        CONCATENATE 'http://' host ':' service '/' index '/' type '/' INTO url_base.
      ENDIF.

  ENDMETHOD.
  