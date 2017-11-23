
SELECT U1.FIRST_NAME, U1.LAST_NAME, U2.FIRST_NAME AS FRIEND_FIRST_NAME, U2.LAST_NAME AS FRIEND_LAST_NAME FROM USERS U1
JOIN FRIENDSHIPS F
ON U1.ID = F.USER_ID
JOIN USERS U2
ON F.FRIEND_ID = U1.ID