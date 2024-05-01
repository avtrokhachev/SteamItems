#!/bin/bash
docker build api/ -t cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_api:latest
docker build worker/ -t cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_worker:latest
docker push cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_api:latest
docker push cr.yandex/crpoqe2ki2gq5j0p88mp/steam_items_worker:latest