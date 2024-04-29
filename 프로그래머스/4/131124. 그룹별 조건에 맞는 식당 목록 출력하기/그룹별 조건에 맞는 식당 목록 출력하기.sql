select a.MEMBER_NAME,b.REVIEW_TEXT,date_format(b.REVIEW_DATE,'%Y-%m-%d') as 'REVIEW_DATE'
from MEMBER_PROFILE a join REST_REVIEW b
using(member_id)
where a.member_id =(
select member_id
    from rest_review 
    group by member_id
    order by count(*) desc
    limit 1
    )

order  by 3,2