export const SALA_MIEJSCA = [
  {
    id: 1,
    rows: 7,
    columns: 12
  },
  {
    id: 2,
    rows: 8,
    columns: 14
  }
];

export const FILMS = [
  {
    id: 1,
    title: "Lighthouse",
    description:
      "Historia dwóch strażników latarni morskiej, którzy w obliczu samotności powoli tracą zdrowie psychiczne, a wkrótce zaczynają im zagrażać ich własne najgorsze koszmary.",
    plot:
      "Robert Eggers, wizjonerski reżyser arcydzielnego horroru The Witch, powraca z hipnotyzującą, halucynującą opowieścią o dwóch latarnikach, pracujących na tajemniczej, odległej wyspie w Nowej Anglii, w latach dziewięćdziesiątych XIX wieku. Obaj latarnicy (Willem Dafoe i Robert Pattinson) mierzą się z samotnością i odosobnieniem podczas wielkiego sztormu, który wydaje się nie mieć końca. Są skazani na walkę z własną silną wolą, potrzebami oraz – przede wszystkim – z tajemniczą siłą, która nad nimi krąży, ale której istnienie może im się tylko wydawać… Film jest przerażającą, pełną tajemnic podróżą w nieznane",
    rating: 4,
    time: 90
  },
  {
    id: 2,
    title: "Irlandczyk",
    description:
      "Płatny zabójca Frank Sheeran powraca do sekretów, których strzegł jako lojalny członek rodziny przestępczej Bufalino.",
    plot:
      ' "Irlandczyk" to osadzona w powojennej Ameryce epicka opowieść widziana oczami weterana II wojny światowej Franka Sheerana, oszusta i płatnego mordercy pracującego dla najbardziej osławionych przestępców XX wieku. Rozgrywająca się na przestrzeni kilkudziesięciu lat saga poświęcona jest jednej z największych zagadek kryminalnych w historii Stanów Zjednoczonych – tajemniczemu zaginięciu legendarnego przywódcy związków zawodowych Jimmy’ego Hoffa. Widzowie wezmą udział w brutalnej podróży, podczas której zostaną przed nimi odsłonięte kulisy funkcjonowania przestępczego półświatka, wewnętrznych walk o wpływy oraz kryminalnych powiązań ze światem polityki.',
    rating: 8,
    time: 180
  },
  {
    id: 3,
    title: "Kraina lodu II",
    description:
      "Elsa i Anna wraz z przyjaciółmi udają się do Zaczarowanego Lasu w poszukiwaniu pomocy dla swego Królestwa.",
    plot:
      "Akcja kontynuacji filmu jest osadzona trzy lata po wydarzeniach z pierwszej części. W Arendelle panuje ład pod panowaniem Elsy, jednak królowa zaczyna słyszeć dziwny głos, który nawołuje ją z północy. Wraz z Anną, Kristoffem i Olafem postanawiają wyruszyć w drogę, aby poznać prawdę o tym, co przywołuję Elsę i odkryć prawdę o jej mocach. Chociaż nie jest to na razie potwierdzone, nowy zwiastun animacji sugeruje, jakoby Anna również posiadała magiczne moce! Co więcej, wygląda to, jakby siostra Elsy była w stanie władać... ogniem!",
    rating: 6,
    time: 90
  },
  {
    id: 4,
    title: "Doktor Sen",
    description:
      'Lata po wydarzeniach z "Lśnienia", dorosły Dan Torrence spotyka młodą dziewczynę o podobnych mocach do jego. Próbuje ją chronić przed kultem zwanym "Prawdziwym węzłem", którego wyznawcy polują na dzieci. ',
    plot:
      'Minęło wiele lat od czasu wydarzeń, które rozegrały się w "Lśnieniu". Dorosły już Dan Torrence (Ewan McGregor) spotyka dziewczynkę, która przejawia podobne do niego zdolności. Stara się ją chronić przed kultem o nazwie Prawdziwy Węzeł, którego członkowie polują na dzieci obdarzone mocami, aby zachować nieśmiertelność.',
    rating: 6,
    time: 90
  }
  // {
  //   id: 5,
  //   title: "Nadzwyczajni",
  //   description:
  //     "Bruno i Malik są najlepszymi kumplami, którzy od dwudziestu lat czynnie działają na rzecz autystycznych dzieci i młodzieży. W prowadzonych przez siebie ośrodkach szkolą młodych ludzi z trudnych dzielnic, aby ci fachowo zajmowali się trudnymi przypadkami.",
  //   plot:
  //     "Bruno (Vincent Cassel) i Malik (Reda Kateb) są najlepszymi kumplami. Na pierwszy rzut oka wszystko ich dzieli – temperament, zainteresowania, a nawet religia. Łączy natomiast gorąca przyjaźń oraz fakt, że od dwudziestu lat czynnie działają na rzecz autystycznych dzieci i młodzieży. W prowadzonych przez siebie ośrodkach szkolą młodych ludzi z trudnych dzielnic, aby ci fachowo zajmowali się przypadkami zakwalifikowanymi przez medycynę jako trudne i złożone. Nie wszystkim jednak metody Bruno i Malika są w smak. Kiedy Inspektorat Opieki Społecznej bierze pod lupę ich działalności i grozi zamknięciem ośrodków, przyjaciele rozpoczynają nierówną walkę z systemem. Wszystko dla dobra i zdrowia swoich niezwykłych podopiecznych.",
  //   rating: 8,
  //   time: 180
  // }
];

export const SEANS = [
  {
    id: 1,
    film: FILMS[1],
    sala: SALA_MIEJSCA[1],
    date: "20-03-2021",
    time: "09:50"
  },
  {
    id: 2,
    film: FILMS[2],
    sala: SALA_MIEJSCA[0],
    date: "20-03-2021",
    time: "12:50"
  },
  {
    id: 3,
    film: FILMS[3],
    sala: SALA_MIEJSCA[0],
    date: "20-03-2021",
    time: "12:50"
  },
  {
    id: 4,
    film: FILMS[3],
    sala: SALA_MIEJSCA[1],
    date: "21-03-2021",
    time: "09:50"
  },
  {
    id: 5,
    film: FILMS[0],
    sala: SALA_MIEJSCA[1],
    date: "20-03-2021",
    time: "09:50"
  }
];
