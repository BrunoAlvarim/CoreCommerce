echo "Esperando banco ficar pronto..."
for i in {1..6}; do
  python manage.py migrate && break
  echo "Banco não pronto, tentando novamente em 5s..."
  sleep 5
done
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "Iniciando servidor..."
gunicorn core.wsgi:application
