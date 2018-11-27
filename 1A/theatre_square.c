#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

int main(int argc, char *argv) {
  uint64_t n, m, a, answer = 0;
  scanf("%lu%lu%lu",&n,&m,&a);
  if ( n%a == 0) {
    answer = n/a;
  } else {
    answer = n/a + 1;
  }
  if ( m%a == 0) {
    answer = answer * m/a;
  } else {
    answer = answer * ( m/a + 1);
  }
  printf("%lu\n",answer);
  return 0;
}
