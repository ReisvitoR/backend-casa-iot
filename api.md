---
title: Casa IoT API v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="casa-iot-api">Casa IoT API v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Documentação da API do backend Casa IoT

# Authentication

- HTTP Authentication, scheme: basic 

* API Key (cookieAuth)
    - Parameter Name: **sessionid**, in: cookie. 

<h1 id="casa-iot-api-api">api</h1>

## api_acaos_list

<a id="opIdapi_acaos_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/acaos/ \
  -H 'Accept: application/json'

```

```http
GET /api/acaos/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/acaos/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/acaos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/acaos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/acaos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/acaos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/acaos/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "ordem": -2147483648,
    "intervalo_tempo": 0.1,
    "estado_desejado": true,
    "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
    "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
  }
]
```

<h3 id="api_acaos_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_acaos_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AcaoCena](#schemaacaocena)]|false|none|none|
|» id|string(uuid)|true|read-only|none|
|» ordem|integer|true|none|none|
|» intervalo_tempo|number(double)¦null|false|none|none|
|» estado_desejado|boolean|true|none|none|
|» dispositivo|string(uuid)|true|none|none|
|» cena|string(uuid)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_acaos_create

<a id="opIdapi_acaos_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/acaos/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/acaos/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/acaos/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/acaos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/acaos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/acaos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/acaos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/acaos/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

> Body parameter

```json
{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

```yaml
ordem: -2147483648
intervalo_tempo: 0.1
estado_desejado: true
dispositivo: d5be3720-1a88-4d0b-af58-d753afd3a9f9
cena: 600b9c88-eb91-4559-a8f6-28e0fab3e77f

```

<h3 id="api_acaos_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AcaoCena](#schemaacaocena)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

<h3 id="api_acaos_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[AcaoCena](#schemaacaocena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_acaos_retrieve

<a id="opIdapi_acaos_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/acaos/{id}/ \
  -H 'Accept: application/json'

```

```http
GET /api/acaos/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/acaos/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/acaos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/acaos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/acaos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/acaos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/acaos/{id}/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

<h3 id="api_acaos_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this acao cena.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

<h3 id="api_acaos_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[AcaoCena](#schemaacaocena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_acaos_update

<a id="opIdapi_acaos_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/acaos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/acaos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/acaos/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/acaos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/acaos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/acaos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/acaos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/acaos/{id}/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

> Body parameter

```json
{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

```yaml
ordem: -2147483648
intervalo_tempo: 0.1
estado_desejado: true
dispositivo: d5be3720-1a88-4d0b-af58-d753afd3a9f9
cena: 600b9c88-eb91-4559-a8f6-28e0fab3e77f

```

<h3 id="api_acaos_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this acao cena.|
|body|body|[AcaoCena](#schemaacaocena)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

<h3 id="api_acaos_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[AcaoCena](#schemaacaocena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_acaos_partial_update

<a id="opIdapi_acaos_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/acaos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PATCH /api/acaos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/acaos/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.patch '/api/acaos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/api/acaos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/acaos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/acaos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/acaos/{id}/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

> Body parameter

```json
{
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

```yaml
ordem: -2147483648
intervalo_tempo: 0.1
estado_desejado: true
dispositivo: d5be3720-1a88-4d0b-af58-d753afd3a9f9
cena: 600b9c88-eb91-4559-a8f6-28e0fab3e77f

```

<h3 id="api_acaos_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this acao cena.|
|body|body|[PatchedAcaoCena](#schemapatchedacaocena)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}
```

<h3 id="api_acaos_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[AcaoCena](#schemaacaocena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_acaos_destroy

<a id="opIdapi_acaos_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/acaos/{id}/

```

```http
DELETE /api/acaos/{id}/ HTTP/1.1

```

```javascript

fetch('/api/acaos/{id}/',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/acaos/{id}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/acaos/{id}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/acaos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/acaos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/acaos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/acaos/{id}/`

retrieve:
Retorna uma ação de cena específica pelo ID.

list:
Lista todas as ações de cena cadastradas.

create:
Cria uma nova ação de cena.

update:
Atualiza uma ação de cena existente.

partial_update:
Atualiza parcialmente uma ação de cena existente.

destroy:
Remove uma ação de cena.

<h3 id="api_acaos_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this acao cena.|

<h3 id="api_acaos_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_list

<a id="opIdapi_cenas_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/cenas/ \
  -H 'Accept: application/json'

```

```http
GET /api/cenas/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/cenas/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/cenas/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/cenas/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/cenas/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/cenas/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/cenas/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "nome": "string",
    "ativa": true,
    "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
  }
]
```

<h3 id="api_cenas_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_cenas_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Cena](#schemacena)]|false|none|none|
|» id|string(uuid)|true|read-only|none|
|» nome|string|true|none|none|
|» ativa|boolean|false|none|none|
|» usuario|string(uuid)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_create

<a id="opIdapi_cenas_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/cenas/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/cenas/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/cenas/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/cenas/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/cenas/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/cenas/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/cenas/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/cenas/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

> Body parameter

```json
{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
ativa: true
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_cenas_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Cena](#schemacena)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_cenas_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Cena](#schemacena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_retrieve

<a id="opIdapi_cenas_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/cenas/{id}/ \
  -H 'Accept: application/json'

```

```http
GET /api/cenas/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/cenas/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/cenas/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/cenas/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/cenas/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/cenas/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/cenas/{id}/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

<h3 id="api_cenas_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this cena.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_cenas_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Cena](#schemacena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_update

<a id="opIdapi_cenas_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/cenas/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/cenas/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/cenas/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/cenas/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/cenas/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/cenas/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/cenas/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/cenas/{id}/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

> Body parameter

```json
{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
ativa: true
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_cenas_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this cena.|
|body|body|[Cena](#schemacena)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_cenas_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Cena](#schemacena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_partial_update

<a id="opIdapi_cenas_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/cenas/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PATCH /api/cenas/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/cenas/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.patch '/api/cenas/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/api/cenas/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/cenas/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/cenas/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/cenas/{id}/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

> Body parameter

```json
{
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
ativa: true
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_cenas_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this cena.|
|body|body|[PatchedCena](#schemapatchedcena)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_cenas_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Cena](#schemacena)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_cenas_destroy

<a id="opIdapi_cenas_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/cenas/{id}/

```

```http
DELETE /api/cenas/{id}/ HTTP/1.1

```

```javascript

fetch('/api/cenas/{id}/',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/cenas/{id}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/cenas/{id}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/cenas/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/cenas/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/cenas/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/cenas/{id}/`

retrieve:
Retorna uma cena específica pelo ID.

list:
Lista todas as cenas cadastradas.

create:
Cria uma nova cena.

update:
Atualiza uma cena existente.

partial_update:
Atualiza parcialmente uma cena existente.

destroy:
Remove uma cena.

<h3 id="api_cenas_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this cena.|

<h3 id="api_cenas_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_list

<a id="opIdapi_comodos_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/comodos/ \
  -H 'Accept: application/json'

```

```http
GET /api/comodos/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/comodos/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/comodos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/comodos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/comodos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/comodos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/comodos/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "nome": "string",
    "background_url": "string",
    "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
  }
]
```

<h3 id="api_comodos_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_comodos_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Comodo](#schemacomodo)]|false|none|none|
|» id|string(uuid)|true|read-only|none|
|» nome|string|true|none|none|
|» background_url|string¦null|false|none|none|
|» usuario|string(uuid)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_create

<a id="opIdapi_comodos_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/comodos/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/comodos/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/comodos/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/comodos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/comodos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/comodos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/comodos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/comodos/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

> Body parameter

```json
{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
background_url: string
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_comodos_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Comodo](#schemacomodo)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_comodos_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Comodo](#schemacomodo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_retrieve

<a id="opIdapi_comodos_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/comodos/{id}/ \
  -H 'Accept: application/json'

```

```http
GET /api/comodos/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/comodos/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/comodos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/comodos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/comodos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/comodos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/comodos/{id}/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

<h3 id="api_comodos_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this comodo.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_comodos_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comodo](#schemacomodo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_update

<a id="opIdapi_comodos_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/comodos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/comodos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/comodos/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/comodos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/comodos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/comodos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/comodos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/comodos/{id}/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

> Body parameter

```json
{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
background_url: string
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_comodos_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this comodo.|
|body|body|[Comodo](#schemacomodo)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_comodos_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comodo](#schemacomodo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_partial_update

<a id="opIdapi_comodos_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/comodos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PATCH /api/comodos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/comodos/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.patch '/api/comodos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/api/comodos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/comodos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/comodos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/comodos/{id}/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

> Body parameter

```json
{
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

```yaml
nome: string
background_url: string
usuario: 9ca26181-8402-4bf6-8f0e-6070f8975089

```

<h3 id="api_comodos_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this comodo.|
|body|body|[PatchedComodo](#schemapatchedcomodo)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}
```

<h3 id="api_comodos_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Comodo](#schemacomodo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_comodos_destroy

<a id="opIdapi_comodos_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/comodos/{id}/

```

```http
DELETE /api/comodos/{id}/ HTTP/1.1

```

```javascript

fetch('/api/comodos/{id}/',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/comodos/{id}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/comodos/{id}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/comodos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/comodos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/comodos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/comodos/{id}/`

retrieve:
Retorna um cômodo específico pelo ID.

list:
Lista todos os cômodos cadastrados.

create:
Cria um novo cômodo.

update:
Atualiza um cômodo existente.

partial_update:
Atualiza parcialmente um cômodo existente.

destroy:
Remove um cômodo.

<h3 id="api_comodos_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this comodo.|

<h3 id="api_comodos_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_list

<a id="opIdapi_dispositivos_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/dispositivos/ \
  -H 'Accept: application/json'

```

```http
GET /api/dispositivos/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/dispositivos/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/dispositivos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/dispositivos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/dispositivos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/dispositivos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/dispositivos/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "nome": "string",
    "estado": true,
    "tipo": "string",
    "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
  }
]
```

<h3 id="api_dispositivos_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_dispositivos_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Dispositivo](#schemadispositivo)]|false|none|none|
|» id|string(uuid)|true|read-only|none|
|» nome|string|true|none|none|
|» estado|boolean|false|none|none|
|» tipo|string|true|none|none|
|» comodo|string(uuid)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_create

<a id="opIdapi_dispositivos_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/dispositivos/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/dispositivos/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/dispositivos/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/dispositivos/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/dispositivos/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/dispositivos/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/dispositivos/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/dispositivos/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

> Body parameter

```json
{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

```yaml
nome: string
estado: true
tipo: string
comodo: bc0e7341-78af-417f-92d8-2dc7279a1708

```

<h3 id="api_dispositivos_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Dispositivo](#schemadispositivo)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

<h3 id="api_dispositivos_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Dispositivo](#schemadispositivo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_retrieve

<a id="opIdapi_dispositivos_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/dispositivos/{id}/ \
  -H 'Accept: application/json'

```

```http
GET /api/dispositivos/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/dispositivos/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/dispositivos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/dispositivos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/dispositivos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/dispositivos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/dispositivos/{id}/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

<h3 id="api_dispositivos_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this dispositivo.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

<h3 id="api_dispositivos_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Dispositivo](#schemadispositivo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_update

<a id="opIdapi_dispositivos_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/dispositivos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/dispositivos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/dispositivos/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/dispositivos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/dispositivos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/dispositivos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/dispositivos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/dispositivos/{id}/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

> Body parameter

```json
{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

```yaml
nome: string
estado: true
tipo: string
comodo: bc0e7341-78af-417f-92d8-2dc7279a1708

```

<h3 id="api_dispositivos_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this dispositivo.|
|body|body|[Dispositivo](#schemadispositivo)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

<h3 id="api_dispositivos_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Dispositivo](#schemadispositivo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_partial_update

<a id="opIdapi_dispositivos_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/dispositivos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PATCH /api/dispositivos/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/dispositivos/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.patch '/api/dispositivos/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/api/dispositivos/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/dispositivos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/dispositivos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/dispositivos/{id}/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

> Body parameter

```json
{
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

```yaml
nome: string
estado: true
tipo: string
comodo: bc0e7341-78af-417f-92d8-2dc7279a1708

```

<h3 id="api_dispositivos_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this dispositivo.|
|body|body|[PatchedDispositivo](#schemapatcheddispositivo)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}
```

<h3 id="api_dispositivos_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Dispositivo](#schemadispositivo)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_dispositivos_destroy

<a id="opIdapi_dispositivos_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/dispositivos/{id}/

```

```http
DELETE /api/dispositivos/{id}/ HTTP/1.1

```

```javascript

fetch('/api/dispositivos/{id}/',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/dispositivos/{id}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/dispositivos/{id}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/dispositivos/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/dispositivos/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/dispositivos/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/dispositivos/{id}/`

retrieve:
Retorna um dispositivo específico pelo ID.

list:
Lista todos os dispositivos cadastrados.

create:
Cria um novo dispositivo.

update:
Atualiza um dispositivo existente.

partial_update:
Atualiza parcialmente um dispositivo existente.

destroy:
Remove um dispositivo.

<h3 id="api_dispositivos_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this dispositivo.|

<h3 id="api_dispositivos_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_schema_retrieve

<a id="opIdapi_schema_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/schema/ \
  -H 'Accept: application/vnd.oai.openapi'

```

```http
GET /api/schema/ HTTP/1.1

Accept: application/vnd.oai.openapi

```

```javascript

const headers = {
  'Accept':'application/vnd.oai.openapi'
};

fetch('/api/schema/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/vnd.oai.openapi'
}

result = RestClient.get '/api/schema/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/vnd.oai.openapi'
}

r = requests.get('/api/schema/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/vnd.oai.openapi',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/schema/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/schema/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/vnd.oai.openapi"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/schema/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/schema/`

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

<h3 id="api_schema_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|format|query|string|false|none|
|lang|query|string|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|format|json|
|format|yaml|
|lang|af|
|lang|ar|
|lang|ar-dz|
|lang|ast|
|lang|az|
|lang|be|
|lang|bg|
|lang|bn|
|lang|br|
|lang|bs|
|lang|ca|
|lang|ckb|
|lang|cs|
|lang|cy|
|lang|da|
|lang|de|
|lang|dsb|
|lang|el|
|lang|en|
|lang|en-au|
|lang|en-gb|
|lang|eo|
|lang|es|
|lang|es-ar|
|lang|es-co|
|lang|es-mx|
|lang|es-ni|
|lang|es-ve|
|lang|et|
|lang|eu|
|lang|fa|
|lang|fi|
|lang|fr|
|lang|fy|
|lang|ga|
|lang|gd|
|lang|gl|
|lang|he|
|lang|hi|
|lang|hr|
|lang|hsb|
|lang|hu|
|lang|hy|
|lang|ia|
|lang|id|
|lang|ig|
|lang|io|
|lang|is|
|lang|it|
|lang|ja|
|lang|ka|
|lang|kab|
|lang|kk|
|lang|km|
|lang|kn|
|lang|ko|
|lang|ky|
|lang|lb|
|lang|lt|
|lang|lv|
|lang|mk|
|lang|ml|
|lang|mn|
|lang|mr|
|lang|ms|
|lang|my|
|lang|nb|
|lang|ne|
|lang|nl|
|lang|nn|
|lang|os|
|lang|pa|
|lang|pl|
|lang|pt|
|lang|pt-br|
|lang|ro|
|lang|ru|
|lang|sk|
|lang|sl|
|lang|sq|
|lang|sr|
|lang|sr-latn|
|lang|sv|
|lang|sw|
|lang|ta|
|lang|te|
|lang|tg|
|lang|th|
|lang|tk|
|lang|tr|
|lang|tt|
|lang|udm|
|lang|ug|
|lang|uk|
|lang|ur|
|lang|uz|
|lang|vi|
|lang|zh-hans|
|lang|zh-hant|

> Example responses

> 200 Response

```json
{
  "property1": null,
  "property2": null
}
```

<h3 id="api_schema_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_schema_retrieve-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» **additionalProperties**|any|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_list

<a id="opIdapi_usuarios_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/usuarios/ \
  -H 'Accept: application/json'

```

```http
GET /api/usuarios/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/usuarios/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/usuarios/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/usuarios/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/usuarios/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/usuarios/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/usuarios/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "email": "user@example.com",
    "senha_hash": "string"
  }
]
```

<h3 id="api_usuarios_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_usuarios_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Usuario](#schemausuario)]|false|none|none|
|» id|string(uuid)|true|read-only|none|
|» email|string(email)|true|none|none|
|» senha_hash|string|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_create

<a id="opIdapi_usuarios_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/usuarios/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/usuarios/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "email": "user@example.com",
  "senha_hash": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/usuarios/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/usuarios/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/usuarios/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/usuarios/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/usuarios/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/usuarios/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

> Body parameter

```json
{
  "email": "user@example.com",
  "senha_hash": "string"
}
```

```yaml
email: user@example.com
senha_hash: string

```

<h3 id="api_usuarios_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Usuario](#schemausuario)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}
```

<h3 id="api_usuarios_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Usuario](#schemausuario)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_retrieve

<a id="opIdapi_usuarios_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/usuarios/{id}/ \
  -H 'Accept: application/json'

```

```http
GET /api/usuarios/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/api/usuarios/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/api/usuarios/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/usuarios/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/usuarios/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/usuarios/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/usuarios/{id}/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

<h3 id="api_usuarios_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this usuario.|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}
```

<h3 id="api_usuarios_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Usuario](#schemausuario)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_update

<a id="opIdapi_usuarios_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/usuarios/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /api/usuarios/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "email": "user@example.com",
  "senha_hash": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/usuarios/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/api/usuarios/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/usuarios/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/usuarios/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/usuarios/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/usuarios/{id}/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

> Body parameter

```json
{
  "email": "user@example.com",
  "senha_hash": "string"
}
```

```yaml
email: user@example.com
senha_hash: string

```

<h3 id="api_usuarios_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this usuario.|
|body|body|[Usuario](#schemausuario)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}
```

<h3 id="api_usuarios_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Usuario](#schemausuario)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_partial_update

<a id="opIdapi_usuarios_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/usuarios/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PATCH /api/usuarios/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "email": "user@example.com",
  "senha_hash": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/usuarios/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.patch '/api/usuarios/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('/api/usuarios/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/usuarios/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/usuarios/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/usuarios/{id}/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

> Body parameter

```json
{
  "email": "user@example.com",
  "senha_hash": "string"
}
```

```yaml
email: user@example.com
senha_hash: string

```

<h3 id="api_usuarios_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this usuario.|
|body|body|[PatchedUsuario](#schemapatchedusuario)|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}
```

<h3 id="api_usuarios_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Usuario](#schemausuario)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_usuarios_destroy

<a id="opIdapi_usuarios_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/usuarios/{id}/

```

```http
DELETE /api/usuarios/{id}/ HTTP/1.1

```

```javascript

fetch('/api/usuarios/{id}/',
{
  method: 'DELETE'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.delete '/api/usuarios/{id}/',
  params: {
  }

p JSON.parse(result)

```

```python
import requests

r = requests.delete('/api/usuarios/{id}/')

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/usuarios/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/usuarios/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/usuarios/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/usuarios/{id}/`

retrieve:
Retorna um usuário específico pelo ID.

list:
Lista todos os usuários cadastrados.

create:
Cria um novo usuário.

update:
Atualiza um usuário existente.

partial_update:
Atualiza parcialmente um usuário existente.

destroy:
Remove um usuário.

<h3 id="api_usuarios_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this usuario.|

<h3 id="api_usuarios_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

# Schemas

<h2 id="tocS_AcaoCena">AcaoCena</h2>
<!-- backwards compatibility -->
<a id="schemaacaocena"></a>
<a id="schema_AcaoCena"></a>
<a id="tocSacaocena"></a>
<a id="tocsacaocena"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|ordem|integer|true|none|none|
|intervalo_tempo|number(double)¦null|false|none|none|
|estado_desejado|boolean|true|none|none|
|dispositivo|string(uuid)|true|none|none|
|cena|string(uuid)|true|none|none|

<h2 id="tocS_Cena">Cena</h2>
<!-- backwards compatibility -->
<a id="schemacena"></a>
<a id="schema_Cena"></a>
<a id="tocScena"></a>
<a id="tocscena"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|nome|string|true|none|none|
|ativa|boolean|false|none|none|
|usuario|string(uuid)|true|none|none|

<h2 id="tocS_Comodo">Comodo</h2>
<!-- backwards compatibility -->
<a id="schemacomodo"></a>
<a id="schema_Comodo"></a>
<a id="tocScomodo"></a>
<a id="tocscomodo"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|nome|string|true|none|none|
|background_url|string¦null|false|none|none|
|usuario|string(uuid)|true|none|none|

<h2 id="tocS_Dispositivo">Dispositivo</h2>
<!-- backwards compatibility -->
<a id="schemadispositivo"></a>
<a id="schema_Dispositivo"></a>
<a id="tocSdispositivo"></a>
<a id="tocsdispositivo"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|nome|string|true|none|none|
|estado|boolean|false|none|none|
|tipo|string|true|none|none|
|comodo|string(uuid)|true|none|none|

<h2 id="tocS_PatchedAcaoCena">PatchedAcaoCena</h2>
<!-- backwards compatibility -->
<a id="schemapatchedacaocena"></a>
<a id="schema_PatchedAcaoCena"></a>
<a id="tocSpatchedacaocena"></a>
<a id="tocspatchedacaocena"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "ordem": -2147483648,
  "intervalo_tempo": 0.1,
  "estado_desejado": true,
  "dispositivo": "d5be3720-1a88-4d0b-af58-d753afd3a9f9",
  "cena": "600b9c88-eb91-4559-a8f6-28e0fab3e77f"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|ordem|integer|false|none|none|
|intervalo_tempo|number(double)¦null|false|none|none|
|estado_desejado|boolean|false|none|none|
|dispositivo|string(uuid)|false|none|none|
|cena|string(uuid)|false|none|none|

<h2 id="tocS_PatchedCena">PatchedCena</h2>
<!-- backwards compatibility -->
<a id="schemapatchedcena"></a>
<a id="schema_PatchedCena"></a>
<a id="tocSpatchedcena"></a>
<a id="tocspatchedcena"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "ativa": true,
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|nome|string|false|none|none|
|ativa|boolean|false|none|none|
|usuario|string(uuid)|false|none|none|

<h2 id="tocS_PatchedComodo">PatchedComodo</h2>
<!-- backwards compatibility -->
<a id="schemapatchedcomodo"></a>
<a id="schema_PatchedComodo"></a>
<a id="tocSpatchedcomodo"></a>
<a id="tocspatchedcomodo"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "background_url": "string",
  "usuario": "9ca26181-8402-4bf6-8f0e-6070f8975089"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|nome|string|false|none|none|
|background_url|string¦null|false|none|none|
|usuario|string(uuid)|false|none|none|

<h2 id="tocS_PatchedDispositivo">PatchedDispositivo</h2>
<!-- backwards compatibility -->
<a id="schemapatcheddispositivo"></a>
<a id="schema_PatchedDispositivo"></a>
<a id="tocSpatcheddispositivo"></a>
<a id="tocspatcheddispositivo"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "nome": "string",
  "estado": true,
  "tipo": "string",
  "comodo": "bc0e7341-78af-417f-92d8-2dc7279a1708"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|nome|string|false|none|none|
|estado|boolean|false|none|none|
|tipo|string|false|none|none|
|comodo|string(uuid)|false|none|none|

<h2 id="tocS_PatchedUsuario">PatchedUsuario</h2>
<!-- backwards compatibility -->
<a id="schemapatchedusuario"></a>
<a id="schema_PatchedUsuario"></a>
<a id="tocSpatchedusuario"></a>
<a id="tocspatchedusuario"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|read-only|none|
|email|string(email)|false|none|none|
|senha_hash|string|false|none|none|

<h2 id="tocS_Usuario">Usuario</h2>
<!-- backwards compatibility -->
<a id="schemausuario"></a>
<a id="schema_Usuario"></a>
<a id="tocSusuario"></a>
<a id="tocsusuario"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "email": "user@example.com",
  "senha_hash": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|read-only|none|
|email|string(email)|true|none|none|
|senha_hash|string|true|none|none|

