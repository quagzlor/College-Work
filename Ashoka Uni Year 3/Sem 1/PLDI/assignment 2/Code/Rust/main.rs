use std::io;

fn main() {
  let mut input = String::new();

  io::stdin().read_line(&mut input)
      .expect("Couldn't read line");
  let temp_input=input.trim();
  let input_arr = temp_input.split(" ");

  let mut main_arr = vec![0];
  main_arr.pop();

  let mut max_count=0;
  let mut iter_count=0;
  let mut input_vec = vec![0];
  input_vec.pop();
  
  for i in input_arr{
    let myint: i32 = i.parse().unwrap();
    input_vec.push(myint);
    }
    
  

  for i in 0..(input_vec.len()){
    let mut hold_arr= vec![input_vec[i]];
    let mut count=1;

    for j in iter_count..(input_vec.len()){
      if input_vec[j]>hold_arr[count-1]{
        hold_arr.push(input_vec[j]);
        count=count+1;
      }

    }

    if count>max_count{
      max_count=count;
      for k in 0..(main_arr.len()){
        main_arr.pop();
      
      }
      for k in 0..(count){
        main_arr.push(hold_arr[k])
      }
    }
    iter_count=iter_count+1;
  }
  for i in main_arr.iter_mut(){
    print!("{} ",i);
  }
  
}