# firebase_fcm_utls

Para mandar messagens atraves de server python request http/...
>1 Obter o link do servidor de fcm
[](https://fcm.googleapis.com/fcm/send)
# 2 ter achave do seu projecto firebase de cloud messaging: clique no icon de settings e opcion de Configuracoes do projecto
![](server_id.png)

# 2 apos abrira a tela onde tem as tab bares e escolhes a de cloud messaging

![](server_key.png)

ai tens o chave do servidor

# FAZENDO POST COM POSTMAN
precisa token do device/
para obter otoken de FirebaseMessaging nos androids atraves de flutter :
```dart
  getToken() async {
    await FirebaseMessaging.instance.getToken().then((value) {
      print(value);
      Get.defaultDialog(
          content: Column(
        children: [
          Text('Notification Token'),
          TextFormField(
            initialValue: '$value',
          ),
        ],
      ));
    });
  }

```

# No body preecher os dados de notificacao
![](postman_body.png)


# No Headers preecher os dados:
![](postman_headers.png)

>> os mais requeridos

Content-Type : application/json

Authorization : key=chave do servidor do firebase