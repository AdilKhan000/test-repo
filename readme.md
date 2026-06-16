It is recommended to disable all CBC-mode cipher suites on the server. Only the following strong cipher suites should be supported:
TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS 1.3 should be enforced where possible, as it exclusively uses AEAD ciphers and eliminates CBC-mode entirely
