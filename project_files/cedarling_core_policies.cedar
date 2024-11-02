// simple policy example for pricipal workload
permit (
    principal is Jans::Workload,
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
);

// simple policy example for pricipal user
permit (
    principal is Jans::User,
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
);

// simple policy example for pricipal role
permit (
    principal == Jans::Role::"Admin",
    action in [Jans::Action::"Update"],
    resource is Jans::Issue
);