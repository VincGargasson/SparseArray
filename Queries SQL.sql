
"Classement des ventes 2019 par jour"

SELECT   date
        ,ROUND(SUM(prod_price * prod_qty),2) as ventes
FROM TRANSACTIONS
WHERE date BETWEEN '01-01-2019' AND '31-12-2019'
GROUP BY date
ORDER BY date




"Ventes de meubles et déco par clients sur 2019"

SELECT   client_id
        ,SUM(CASE WHEN pn.product_type = 'MEUBLE' THEN ROUND(t.prod_price * t.prod_qty,2) END) as ventes_meuble
        ,SUM(CASE WHEN pn.product_type = 'DECO' THEN ROUND(t.prod_price * t.prod_qty,2) END) as ventes_deco

FROM TRANSACTIONS t
LEFT JOIN PRODUCT_NOMENCLATURE pn
    ON t.prod_id = pn.product_id
WHERE t.date BETWEEN '01-01-2019' AND '31-12-2019'
GROUP BY client_id