#!/bin/bash

input_dates=`cat $1`
#echo "$input_dates"

start_date=`echo $input_dates | cut -d',' -f1`
end_date=`echo $input_dates | cut -d',' -f2`


start_month=`echo $start_date|cut -d'-' -f2`
start_year=`echo $start_date|cut -d'-' -f3`

end_month=`echo $end_date|cut -d'-' -f2`
end_year=`echo $end_date|cut -d'-' -f3`

echo $start_month $start_year $end_month $end_year

month_end=`expr $end_month \* 1`

function dbExecute()
{
echo "Inside the function, Parameter Passed: $1"

}


loops=0
target_loops=`expr $end_year - $start_year`
#echo "No Of Loops: $target_loops"

j=`expr $start_month \* 1`

for (( i = $start_year; i <= $end_year; i++ ))
do 
#echo "Year = $i Loop $loops "
#for (( j = $start_month; j <= 12; j+=2 )) 
while [ $j -le 12  ]
do
if [ $start_year == $end_year ] ||  [ $i == $end_year -a $end_month == 12 ] || [ $i == $start_year  ] || [ $i != $end_year  ];
then
case $j in 

1)monthrange="'"JAN$i"'","'"FEB$i"'"
dbExecute $monthrange;;
2)monthrange="'"FEB$i"'","'"MAR$i"'"
dbExecute $monthrange;;
3)monthrange="'"MAR$i"'","'"APR$i"'"
dbExecute $monthrange;;
4)monthrange="'"APR$i"'","'"MAY$i"'"
dbExecute $monthrange;;
5)monthrange="'"MAY$i"'","'"JUN$i"'"
dbExecute $monthrange;;
6)monthrange="'"JUN$i"'","'"JUL$i"'"
dbExecute $monthrange;;
7)monthrange="'"JUL$i"'","'"AUG$i"'"
dbExecute $monthrange;;
8)monthrange="'"AUG$i"'","'"SEP$i"'"
dbExecute $monthrange;;
9)monthrange="'"SEP$i"'","'"OCT$i"'"
dbExecute $monthrange;;
10)monthrange="'"OCT$i"'","'"NOV$i"'"
dbExecute $monthrange;;
11)monthrange="'"NOV$i"'","'"DEC$i"'"
dbExecute $monthrange;;
12)monthrange="'"DEC$i"'"
dbExecute $monthrange;;
esac

else

case $j in

1)monthrange="'"JAN$i"'"
dbExecute $monthrange;;
3)monthrange="'"FEB$i"'","'"MAR$i"'"
dbExecute $monthrange;;
5)monthrange="'"APR$i"'","'"MAY$i"'"
dbExecute $monthrange;;
7)monthrange="'"JUN$i"'","'"JUL$i"'"
dbExecute $monthrange;;
9)monthrange="'"AUG$i"'","'"SEP$i"'"
dbExecute $monthrange;;
11)monthrange="'"OCT$i"'","'"NOV$i"'"
dbExecute $monthrange;;

esac

fi
if [ $target_loops == $loops -a $j -ge $month_end ];
then
break
fi

j=`expr $j + 2`
#echo "Value of J is $j, Month End is $month_end"

#j=`expr $j + 2`

done

j=1
loops=`expr $loops + 1`
done


