1. a multi container minikube or microk8s 
    appc/dd.ynl

    nginx for frontend (replace this with nginx ingress controller)
    react app
    flask + (optional nginx with local location)
    redis pod 

    ```bash
    (base) anirban@Nothing-To-Look-Here apps % k get all -n test
NAME                      READY   STATUS    RESTARTS   AGE
pod/dd-597655f5cb-kspxz   4/4     Running   17         12h

NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                    AGE
service/redis-svc   ClusterIP   10.106.69.140   <none>        80/TCP,6379/TCP,8081/TCP   13h

NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/dd   1         1         1            1           13h

NAME                            DESIRED   CURRENT   READY   AGE
replicaset.apps/dd-597655f5cb   1         1         1       12h
replicaset.apps/dd-869fbb885    0         0         0       13h
(base) anirban@Nothing-To-Look-Here apps % 
    ```

    flask app is an updated https://github.com/jazzdd86/alpine-flask/
    with flask_cors & redis client
    
    React form takes in a username in a form and updates a redis cache

    port forward to access minikube (todo: ingress controller + metalb)

    ```bash
    (base) anirban@Nothing-To-Look-Here appc % k port-forward service/redis-svc 8088:80 -n test
Forwarding from 127.0.0.1:8088 -> 80
Forwarding from [::1]:8088 -> 80
Handling connection for 8088
Handling connection for 8088
Handling connection for 8088

    ```

2. nested.py

    run as 

    ```bash
    python test_nested.py
    ```

3. AZ vm metadata

```bash
    python test_az_meta.py
    ```