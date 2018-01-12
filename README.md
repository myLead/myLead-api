# mylead-api
#implementar documentação
# SocialSecurity API DOC

### URL PADRÃO
```
http://mylead-api.herokuapp.com/user
```



## USERS

### Cadastro de usuário
``` POST: ``` ```users/ ``` 

``` BODY: ``` 
```console
    {
      "nome": "string",
      "email_usuario": "string",
      "senha_usuario": "string",
      "cnpj": "string"
      
    }
```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', message: 'Usuario cadastrado', 'data': {} ```|    

 
### Listagem de usuáiros
``` GET: ``` ```users/ ```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', message: 'Lista de usuarios', 'data': output ```|    


### Listar único usuáiro
``` GET: ``` ```user/ ``` ```id```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', 'message': 'Usuario encontrado', data: user_data} ```|    
| error: | ```status': 'error', message: 'Sem ocorrencias', data: {}'``` |


### Validação de usuáiro
``` GET: ``` ```users/validate/login/ ``` ```users/validate/login/ ```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', data: data, message: 'Usuário cadastrado' ```|    
| error: | ``` status: 'error', data: {}, message: 'Usuáro não cadastrado'``` |



## DEVICES

### Cadastro de device
``` POST: ``` ```device/ ``` 

``` BODY: ``` 
```console
   {
      "cod_device": "string"
   }
```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', data: data, message: 'Inserted device' ```|    


### Validação de device
``` GET: ``` ```device/validate/``` ```id_device ```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', data: data, message: 'Retrieved One users' ```|    
| error: | ``` status: 'error', data: {}, message: 'Usuáro não cadastrado'``` |



## LOGIN


### Efetuar login
``` PUT: ``` ```users/login/ ``` ```id_device ```

``` BODY: ``` 
```console
   {
      "cod_usuario": int
   }
```

| Status   | response |
| -------- | ----------- |
| success: | ```status: 'success', data: data, message: 'logado' ```|    
| error: | ``` status: 'error', data: data, message: 'login não efetuado'``` |
