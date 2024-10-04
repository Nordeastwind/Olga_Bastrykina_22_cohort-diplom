select c.login, count(o."id") as "Количество заказов в работе" from "Couriers" as c inner join "Orders" as o on  o."courierId"=c.id where o."inDelivery" = true group by c.login;
