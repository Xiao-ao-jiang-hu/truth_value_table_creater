#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;


int main()
{
	//prepare
    string input,input_print;
    cout<<"请输入公式（析+，合*，蕴含—>，蕴含于<-,双<=>，否定！，真1，假0，必须加括号"<<endl;
    cin>>input;
    int len=input.length();
    input_print=input;
    int num=0;
    for(int i=0;i<len;i++){
    	int q=1;
        for(int j=0;j<i;j++){
            if(input[i]==input[j]){
                q=0;
                break;
            }
    }
            if(input[i]>='a'&&input[i]<='z'&&q==1){
            	num++;
            }
    }
    //create truth value table
    char character[num];
    int line_count=pow(2,num);
    int table[line_count][num+1];
    int truth_value[num]={0};
	int k=0;
    for(int i=0;i<len;i++){
    	int q=1;
        for(int j=0;j<i;j++){
            if(input[i]==input[j]){
              	q=0;
                break;
            }
        }
        //except invalid character
        if(input[i]>='a'&&input[i]<='z'&&q==1){
         	character[k]=input[i];
          	k++;
        }
    }
    //print"-------"
    sort(character,character+num);
    for(int i=0;i<len+(2*num)+3;i++){
    	cout<<"-" ;
    }
	cout<<endl;
	//print table head
    for(int i=0;i<num;i++){
    	cout<<character[i]<<" ";
    }
    cout<<"| ";
    cout<<input_print<<endl;
    //print"-------"
    for(int i=0;i<len+(2*num)+3;i++){
    	cout<<"-" ;
    }
	cout<<endl;
    int character_number=0;
    while(character_number<pow(2,num)){
    	int m=len;
    	string c=input;

    	for(int i=0;i<num;i++){
    		cout<<truth_value[i]<<" ";
    		table[character_number][i]=truth_value[i];
    	}
    	cout<<"| ";
    	for(int i=0;i<len;i++){
    		for(int j=0;j<num;j++){
    			if(c[i]==character[j]){
    				c[i]=truth_value[j]+'0';
    			}
			}
		}
    	//repalce all the basics,until there's only single element in the list
    	while(m!=1){
    		//not
    		if(c.find("!1")!=string::npos)
	        c=c.replace(c.find("!1"),2,"0");
	        if(c.find("!0")!=string::npos)
	        c=c.replace(c.find("!0"),2,"1");
	        //or
	        if(c.find("1+1")!=string::npos)
	        c=c.replace(c.find("1+1"),3 , "1");
	        if(c.find("1+0")!=string::npos)
	        c=c.replace(c.find("1+0"),3 , "1");
	        if(c.find("0+1")!=string::npos)
	        c=c.replace(c.find("0+1"),3 , "1");
	        if(c.find("0+0")!=string::npos)
	        c=c.replace(c.find("0+0"),3 , "0");
	        //and
	        if(c.find("1*1")!=string::npos)
	        c=c.replace(c.find("1*1"),3 , "1");
	        if(c.find("1*0")!=string::npos)
	        c=c.replace(c.find("1*0"),3 , "0");
	        if(c.find("0*1")!=string::npos)
	        c=c.replace(c.find("0*1"),3 , "0");
	        if(c.find("0*0")!=string::npos)
	        c=c.replace(c.find("0*0"),3 , "0");
	        //yunhan
	        if(c.find("1->1")!=string::npos)
	        c=c.replace(c.find("1->1"),4 , "1");
	        if(c.find("1->0")!=string::npos)
	        c=c.replace(c.find("1->0"),4 , "0");
	        if(c.find("0->1")!=string::npos)
	        c=c.replace(c.find("0->1"),4 , "1");
	        if(c.find("0->0")!=string::npos)
	        c=c.replace(c.find("0->0"),4 , "1");
	        //yunhanyu
	        if(c.find("1<-1")!=string::npos)
	        c=c.replace(c.find("1<-1"),4 , "1");
	        if(c.find("1<-0")!=string::npos)
	        c=c.replace(c.find("1<-0"),4 , "1");
	        if(c.find("0<-1")!=string::npos)
	        c=c.replace(c.find("0<-1"),4 , "0");
	        if(c.find("0<-0")!=string::npos)
	        c=c.replace(c.find("0<-0"),4 , "1");
	        //shuangyunhan
	        if(c.find("1<=>1")!=string::npos)
	        c=c.replace(c.find("1<=>1"),5 , "1");
			if(c.find("1<=>0")!=string::npos)
	        c=c.replace(c.find("1<=>0"),5 , "0");
	        if(c.find("0<=>1")!=string::npos)
	        c=c.replace(c.find("0<=>1"),5 , "0");
	        if(c.find("0<=>0")!=string::npos)
	        c=c.replace(c.find("0<=>0"),5 , "1");
	        //qukuohao
	        if(c.find("(1)")!=string::npos)
	        c=c.replace(c.find("(1)"),3 , "1");
	   	    if(c.find("(0)")!=string::npos)
	        c=c.replace(c.find("(0)"),3 , "0");
	        m=c.length();
	        }
	        for(int i=0;i<(len/2);i++){
	        	cout<<" ";
	        }
	        cout<<c<<endl;
	        if(c=="1"){
	        	table[character_number][num]=1;
	        }
	        else{
	        	table[character_number][num]=0;
	        }
	        truth_value[num-1]=truth_value[num-1]+1;
	        for(int i=num-1;i>=0;i--){
	        	if(truth_value[i]==2){
	        		truth_value[i]=0;
	        		truth_value[i-1]=truth_value[i-1]+1;
	        	}
           }
          character_number++;

    }
    for(int i=0;i<len+(2*num)+3;i++)
	cout<<"-" ;
	cout<<endl;

	int m=0;int M=0;
	for (int i=0;i<line_count;i++){
		if(table[i][num]==1){
			m++;
		}
		else{
			M++;
		}
	}
	return 0;
 }
