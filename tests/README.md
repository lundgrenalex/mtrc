# HOWTO Tests

```bash
. ./setenv.sh;
nose2 --with-coverage  --plugin=nose2.plugins.mp --processes \`nproc\`;
```
