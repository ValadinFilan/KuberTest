# KuberTest


## Запуск через Kubernetes

```
kubectl apply -f .\manifests\ -n <namespace>
```

## Запуск через Helm

```
helm install my-release ./helm-charts/my-web-app -n <namespace>
```