Map<Character,String> save= new HashMap<>();
Map<Character,Node> charNodes; -карта с данными
int sum=0; -сумма введенных значений
int countOfS=0;
int countAl=0; -количество символов в сообщении
class Node implements Comparable<Node>- звено дерева
class InternalNode extends Node -подкласс звена, отвечает за правильное распределение
private void decoder(String s) throws FileNotFoundException
{
  File file=new File("alfabet.txt");
  Scanner input=new Scanner(file);
  while(input.hasNext()) {
    String str = input.next();
    System.out.println(str);
    if(str.contains(":"))
    {
      int i=str.indexOf(":");
      save.put(str.charAt(0),str.substring(i+1));
    }
    else if(countOfS==0)
      countOfS=Integer.parseInt(str);
    else if(countAl==0)
      countAl=Integer.parseInt(str);
    else
    sum=Integer.parseInt(str);
    }
  int c=sum/countOfS;
  System.out.println(c);
  int j=2,i=0;
  String e="";
  while(j<=s.length())
  {
    boolean f=true;
    int d=-1;
    while(f && d<=countAl-1-c) {
      d++;
      for (Map.Entry<Character, String> entry : save.entrySet()) {
        if (s.substring(i, j+d).equals(entry.getValue())||(entry.getValue().equals("0")&&s.substring(i, j+d).equals("00")) ) {
          e += entry.getKey();
          if(entry.getValue().equals("0")&&s.substring(i, j+d).equals("00")){
            e += entry.getKey();
            }
            f = false;
            break;
            }
          }
        }
      j+=d;
      i+=c+d;
      j+=c;
    }
    System.out.println(e);
}
