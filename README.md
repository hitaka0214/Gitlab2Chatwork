Gitlab2Chatwork
======================

# できること

Gitlabから受信したPOSTデータをwebhookで受け，hook2chatwork.pyでChatworkへAPIを送信する。


# 構築方法

* Ubuntu 16.04を使った環境で検証
  vagrant init bento/ubuntu-16.04

## Gitlab-ceをインストール。

http://qiita.com/masakura/items/0a0f00dfdddc8ce27f29

## golangをインストール (adnanh/webhookの実行環境にGoが必要)

http://qiita.com/kent_ocean/items/5bfb7b69973f78b8c843

```
sudo apt-get install golfing
sudo mkdir -p ~/go; echo "export GOPATH=$HOME/go" >> ~/.bashrc
echo "export PATH=$PATH:$HOME/go/bin:/usr/local/go/bin" >> ~/.bashrc
source ~/.bashrc
sudo chown vagrant. /home/vagrant/go
```
   
## adnanh/webhookをインストール

https://github.com/adnanh/webhook

Gitlabから叩かれる用の簡易Webサーバを立てられる。

webhookの設定ファイルをJSON形式で作成。
webhookから起動されるスクリプトを作成。
``hook2chatwork.py``

## Pythonの環境をインストール (Python 2.7.12想定)

```
sudo apt-get install python-pip
pip install requests
Collecting requests
  Downloading requests-2.13.0-py2.py3-none-any.whl (584kB)
    100% |████████████████████████████████| 593kB 1.5MB/s
Installing collected packages: requests
Successfully installed requests
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

## Gitlabのwebhookで取得できるパラメータ

https://docs.gitlab.com/ce/user/project/integrations/webhooks.html
　

## webhook起動

``webhook -hooks hooks.json -verbose``

```　
vagrant@vagrant:~$ webhook -hooks hooks.json -verbose
[webhook] 2017/02/09 16:55:57 version 2.6.0 starting
[webhook] 2017/02/09 16:55:57 setting up os signal watcher
[webhook] 2017/02/09 16:55:57 attempting to load hooks from hooks.json
[webhook] 2017/02/09 16:55:57 found 1 hook(s) in file
[webhook] 2017/02/09 16:55:57      loaded: notificate-to-chatwork
[webhook] 2017/02/09 16:55:57 serving hooks on http://0.0.0.0:9000/hooks/{id}
[webhook] 2017/02/09 16:55:57 os signal watcher ready
```

## GitlabでWebhook設定

該当ProjectのIntegrationsメニューを開く。

```
 URL：http://localhost:9000/hooks/notificate-to-chatwork
 Trigger：Push events，Comments，Issue events, Merge Request eventsにチェック
```

 webhookが叩かれるとパラメータを受け取りながら，スクリプトが呼ばれていることがわかる。

```
[webhook] 2017/02/09 18:24:03 notificate-to-chatwork got matched
[webhook] 2017/02/09 18:24:03 notificate-to-chatwork hook triggered successfully
[webhook] 2017/02/09 18:24:03 2017-02-09T18:24:03Z | 200 |       9.794291ms | localhost:9000 | POST /hooks/notificate-to-chatwork
[webhook] 2017/02/09 18:24:03 executing /home/vagrant/Gitlab2Chatwork/hook2chatwork.py (/home/vagrant/Gitlab2Chatwork/hook2chatwork.py) with arguments ["/home/vagrant/Gitlab2Chatwork/hook2chatwork.py" "issue" "http://vagrant.vm/root/my-awesome-project/issues/4" "open" "Administrator"] and environment [] using /home/vagrant/Gitlab2Chatwork/webhook as cwd
[webhook] 2017/02/09 18:24:04 command output: ['/home/vagrant/Gitlab2Chatwork/main.py', 'issue', 'http://vagrant.vm/root/my-awesome-project/issues/4', 'open', 'Administrator']
'{"message_id":1770302929}'

[webhook] 2017/02/09 18:24:04 finished handling notificate-to-chatwork
```

以上
