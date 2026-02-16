# Heather Syntax Highlighting Examples

This page demonstrates the syntax highlighting for H-hat's Heather dialect.

## Basic Program

```heather
// A simple "hello world" program
main { print("Hello quantum world!") }
```

## Function Definitions

### Simple Function

```heather
fn add(a:i32 b:i32) i32 {
    ::sum(a b)
}
```

### Function with Conditional

```heather
fn factorial(n:u32) u32 {
    if(
        eq(n 0): ::1
        true: ::mul(n factorial(sub(n 1)))
    )
}
```

### Function with Return

```heather
fn max(a:i64 b:i64) i64 {
    if(
        gt(a b): ::a
        true: ::b
    )
}
```

## Type Definitions

### Struct Type

```heather
type point { x:i32 y:i32 }

type person {
    name:str
    age:u32
    active:bool
}
```

### Enum Type

```heather
type status_t { ON OFF }

type result_t {
    data{
        value:i32
    }
    NONE
}
```

### Using Types

```heather
// Declaring and assigning
p:point = .{x=34 y=43}

// Reassigning members
p2<mut>:point
p2.{x=15 y=51}
p2.y = 341

// Enum usage
status:status_t = status_t.ON
result:result_t = result_t.data.value=42
```

## Constants

```heather
const pi:f64 = 3.141592653589793
const e:f64 = 2.718281828459045
const localhost:str = "localhost"
const max_retries:u32 = 5
```

## Quantum Types and Operations

### Quantum Variables

```heather
@q:@bool = @true
@state:@u2 = |0>
@entangled:@bell_t = prepare_bell_state()
```

### Quantum Operations

```heather
fn prepare_superposition(q:@bool) @bool {
    ::hadamard(q)
}

fn entangle(q1:@bool q2:@bool) {
    hadamard(q1)
    cnot(q1 q2)
}
```

### Reflective Cast (Quantum to Classical)

```heather
@q:@bool = hadamard(@false)
classical_result:bool = @q * bool
probability:f64 = @q * f64
```

## Meta-functions

### Option Type (if-like)

```heather
metafn if(options:[opt-body_t]) ir_t {
    // Implementation
}

// Usage
result = if(
    gt(a b): ::a
    true: ::b
)
```

### Body Type (pipe-like)

```heather
metafn pipe(args:[expr_t] body:ir_t) ir_t {
    // Implementation
}

// Usage
pipe(value) {
    double
    add_ten
    print
}
```

### Option-Body Type (match-like)

```heather
metafn match(arg:[expr_t] options:[opt-body_t]) ir_t {
    // Implementation
}

// Usage
match(status) {
    status_t.ON: print("System is ON")
    status_t.OFF: print("System is OFF")
}
```

## Modifiers

### Reference Modifier

```heather
modifier &(self) u32 { ... }

// Usage
value:u32 = 42
ref_value<&>:u32 = &value
```

### Pointer Modifier

```heather
modifier *(self) i64 { ... }

// Usage  
ptr<*>:i64 = *some_value
```

### Mutable Modifier

```heather
// Mutable variable
counter<mut>:u32 = 0
counter = counter + 1
```

### Multiple Modifiers

```heather
mutable_ref<mut &>:point = &p
```

## Imports

### Single Imports

```heather
use(const:math.pi)
use(type:geometry.point)
use(fn:math.add)
```

### Multiple Imports

```heather
use(
    const:math.pi
    const:math.e
    type:geometry.point
    fn:math.add
    fn:math.sub
)
```

### Grouped Imports

```heather
use(
    const:[
        math.pi
        math.e
        math.tau
    ]
    type:[
        geometry.point
        geometry.vector
    ]
)
```

## Traits

### Trait Definition

```heather
#Printable {
    fn print(self) { ... }
}
```

### Using Traits

```heather
type point #Printable {
    x:i32
    y:i32
}

type point #[Printable Serializable] {
    x:i32
    y:i32
}
```

## Complete Example

```heather
// Quantum Bell State Preparation Example
use(
    const:quantum.false
    type:quantum.bell_t
    fn:quantum.hadamard
    fn:quantum.cnot
)

const initial_state:@bool = @false

fn prepare_bell_pair(q1:@bool q2:@bool) @bell_t {
    // Apply Hadamard to first qubit
    hadamard(q1)
    
    // Apply CNOT with q1 as control, q2 as target
    cnot(q1 q2)
    
    // Return the entangled state
    ::.{first=q1 second=q2}
}

fn measure_bell_pair(bell:@bell_t) {
    // Cast quantum state to classical
    result1:bool = bell.first * bool
    result2:bool = bell.second * bool
    
    print("First measurement: " result1)
    print("Second measurement: " result2)
}

main {
    // Initialize qubits
    @q1:@bool = @false
    @q2:@bool = @false
    
    // Prepare Bell state
    @bell:@bell_t = prepare_bell_pair(@q1 @q2)
    
    // Measure
    measure_bell_pair(@bell)
}
```

## Comments

```heather
// This is a single-line comment

/* This is a
   multi-line comment
   spanning several lines */

fn example() {
    // Comments can appear anywhere
    /* Even inline */ value:i32 = 42
}
```

## Operators and Symbols

```heather
// Assignment
value:i32 = 42

// Range
range:i32 = 1..10

// Variadic
fn varargs(args:i32...) { ... }

// Return
fn get_value() i32 { ::42 }

// Cast
result = quantum_data * classical_type

// Reference
ref_val = &value

// Dereference
val = *ptr

// Member access
point.x
person.name

// Nested access
result.data.value
```

## Numbers and Literals

```heather
// Integers
decimal:i32 = 42
negative:i32 = -100
zero:i32 = 0

// Floats
pi:f64 = 3.14159
negative_float:f64 = -2.5

// Quantum integers
@quantum_value:@int = @42

// Booleans
is_active:bool = true
is_disabled:bool = false

// Quantum booleans
@q_true:@bool = @true
@q_false:@bool = @false

// Strings
message:str = "Hello, World!"
path:str = "/home/user/file.txt"
```

---

All code blocks above use the `heather` syntax highlighter, which provides:

- **Keyword highlighting**: `fn`, `type`, `main`, `metafn`, `modifier`, `const`, `use`
- **Type distinction**: Classical types (`i32`, `f64`) vs quantum types (`@bool`, `@int`)
- **Operator highlighting**: `:`, `=`, `::`, `*`, `&`, `...`
- **Comment styling**: Single-line and multi-line comments
- **Number formats**: Integers, floats, and quantum integers
- **String literals**: Double-quoted strings
- **Identifier types**: Regular, quantum (`@var`), and type names
- **Special symbols**: Traits (`#Trait`), modifiers (`<mut>`)
